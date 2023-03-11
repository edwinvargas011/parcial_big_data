from app import download_html,validate_code,validate_hostbyname,validate_upload_page
from unittest.mock import patch
import urllib.request
from unittest.mock import patch
@patch('urllib.request.urlopen')
def test_scraping(mocker): 
    cad='<html><head><title>Chapinero (Bogotá) - 5.588 Inmuebles en Chapinero (Bogotá) - Mitula Casas</title></head><body><p>Este es un ejemplo de HTML</p></body></html>'
    mocker.return_value.read.return_value=cad.encode('utf-8')
    ##Obtiene el titulo de la pagina
    html=download_html("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca") 
    assert html==cad.encode('utf-8')

def test_validate_code():
    ##Validación con codigos de respuesta Trae el titulo de la paginalue="hola") ## medebe retornar este valor verdadero asigno una parte del inico de la pagina
    assert validate_code("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca") in [200,201,202]

def test_validate_hostbyname():
     assert validate_hostbyname("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca")==True
    
def test_validate_upload_page():
    assert validate_upload_page("https://casas.mitula.com.co/searchRE/q-Chapinero--Cundinamarca")==200
  