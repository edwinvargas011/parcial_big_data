import json
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np
import re
import boto3
import os
from datetime import datetime

def f(event, context):
  
  #h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
  #url = requests.get("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca",headers=h,timeout=8)
  
  s3=boto3.client("s3")
  print(s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'])
  print(s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'][0])
  key= s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'][1]['Key']
  html=s3.get_object(Bucket='zappa-1lpoc50kw', Key=key)['Body'].read().decode('utf-8')
  soup = BeautifulSoup(html, "html.parser")
  
  
  data_column={'id':[],'location':[],'type':[],'price':[],'bathrooms':[],'rooms':[],'area':[]}
  
  #print(url.status_code,url.reason,url.headers,url.request.headers)
  
  
  for apto in soup.find_all('div',class_='listing listing-card'):
    data_column['id'].append(apto.get('data-idanuncio'))      #id
    data_column['location'].append(apto.get('data-location')) #location
    data_column['rooms'].append(int(apto.get('data-rooms')))  #num_rooms
    tag_bathroom,tag_area=(apto.find('div',class_="card-icon card-icon__bathrooms"),apto.find('div',class_="card-icon card-icon__area"))
    if(tag_bathroom is not None):
      data_column.get('bathrooms').append(int(tag_bathroom.find_next_sibling('span').text.split(' ')[0]))
    else:
      data_column.get('bathrooms').append(0)
    if(tag_area is None):
      data_column.get('area').append(None)
    else:
      #print(tag_area.find_next_sibling('span').text[:-3])
      data_column.get('area').append(float(tag_area.find_next_sibling('span').text[:-3]))
  
  
  for type_apto in (soup.find_all("span",class_="badge-container__property-type")):
    data_column['type'].append(type_apto.text)
  
  os.chdir('/tmp')
  data_column['price']=[digit for digit in [re.sub('[$.]',"",value.text.replace(" ","")) for value in soup.find_all('div',class_="price")]]
  table_info=pd.DataFrame(data_column)
  print("",table_info.to_csv(datetime.now().strftime('%Y-%m-%d-%r')+'.csv',index = True, header = True))
  print("TABLA_DE ELEMENTOS")
  print(""+table_info.to_csv())

  s3.put_object(Body=table_info.to_csv(),Bucket="zappa-oxd00793r",Key="casas-final-xxx/"+datetime.now().strftime('%Y-%m-%d-%r')+'.csv')
  return {
      'statusCode': 200,
      'body': json.dumps('Función Lambda ejecutada exitosamente')
  }