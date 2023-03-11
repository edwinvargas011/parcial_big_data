import json
import urllib.request 
import boto3
import socket
import requests
import time
from urllib.parse import urlparse
from datetime import datetime
import urllib.request

name_file=""
def f(event, context):
    url="https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca"
    html=urllib.request.urlopen(url).read().decode('utf-8')
    print(html)
    s3=boto3.client('s3')
    s3.put_object(Bucket="zappa-1lpoc50kw",Key="landing-casas-xxx/page33.html",Body=html)
    #urllib.request.urlretrieve(url,'page.html')
    print("Finaliza")
    return {
        'statusCode': 200,
        'body': json.dumps('Función Lambda ejecutada exitosamente')
    }
    


def download_html(mocker):
    
    h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    req = urllib.request.Request("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca")
    response = urllib.request.urlopen(req)
    print("Edwin"+response.getcode())
    print("Edwin_2",response.read())
    return  response.read()

def validate_code(url):
     return urllib.request.urlopen(url).getcode()

def validate_hostbyname(url):
    parsed_url = urlparse(url)
    try:
        socket.gethostbyname(parsed_url.netloc)
        return True
    except socket.error:
        return False

    
def validate_upload_page(url):
    s3=boto3.client("s3")
    html=urllib.request.urlopen("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca").read().decode('utf-8')
    name_file="landing-casas-xxx/"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".html"
    response=s3.put_object(Bucket="zappa-1lpoc50kw",Key=name_file,Body=html)
    return response['ResponseMetadata']['HTTPStatusCode']
    
 