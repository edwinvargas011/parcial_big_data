import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import boto3
import os
from datetime import datetime
import pytz


def f(event, context):
    zone = pytz.timezone('America/Bogota')
    s3 = boto3.client("s3")
    less = datetime.now(zone)-datetime.fromtimestamp(0, zone)
    print(s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'])
    pos = 0
    if (len(s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents']) > 1):
        for i,time in enumerate(list(map(lambda x: x['LastModified'], s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'][1:]))):
            print("ENTRAAAA")
            aux = datetime.now(zone)-time.astimezone(zone)
            if (aux.days < less.days or (aux.days == less.days and aux.seconds < less.seconds)):
                less = aux
                pos = i+1
            print("POS_ "+str(pos))
        key = s3.list_objects_v2(Bucket='zappa-1lpoc50kw')['Contents'][pos].get('Key')
        print(key)
        html = s3.get_object(Bucket='zappa-1lpoc50kw', Key=key)['Body'].read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        data_column = {'FechaDescarga':[],'Id':[],'Barrio':[],'Type':[],'Valor':[],'NumBanos':[],'NumHabitaciones':[],'mts2':[]}
        for apto in soup.find_all('div', class_='listing listing-card'):
            print("Entra cada etiqueta")
            data_column['FechaDescarga'] = data_column['FechaDescarga']+[datetime.now(zone).strftime('%Y-%m-%dz')]
            data_column['Id'].append(apto.get('data-idanuncio'))
            data_column['Barrio'].append(apto.get('data-location'))
            data_column['NumHabitaciones'].append(int(apto.get('data-rooms')))
            tag_bathroom,tag_area = (apto.find('div',class_="card-icon card-icon__bathrooms"),apto.find('div',class_="card-icon card-icon__area"))
            if (tag_bathroom is not None):
                data_column.get('NumBanos').append(int(tag_bathroom.find_next_sibling('span').text.split(' ')[0]))
            else:
                data_column.get('NumBanos').append(0)
            if (tag_area is None):
                data_column.get('mts2').append(None)
            else:
                data_column.get('mts2').append(float(tag_area.find_next_sibling('span').text[:-3]))
        for type_apto in (soup.find_all("span",class_="badge-container__property-type")):
            data_column['Type'].append(type_apto.text)
        os.chdir('/tmp')
        print(data_column)
        data_column['Valor'] = [digit for digit in [re.sub('[$.]',"",value.text.replace(" ","")) for value in soup.find_all('div',class_="price")]]
        table_info = pd.DataFrame(data_column)
        s3.put_object(Body=table_info.to_csv(),Bucket="zappa-oxd00793r",Key="casas-final-xxx/"+datetime.now(zone).strftime('%Y-%m-%d-%r')+'.csv')
    return {
        'statusCode': 200,
        'body': json.dumps('Función Lambda ejecutada exitosamente')}