# Ejecución de la funcion lambda para la descarga del archvio .html
Se realiza web sraping a la pagina de mitula Se codnfigura un veneto a las 10 am de cada lunes, con el fdin de que se realice un trigger hacia la funcipón lmabda y se ejecute la función f, escrita en lenguaje python.
Esta función tiene un desencadenador hacia un bucket s3 que permite guardar la pagina en una carpeta llamada landing-casas-xxx de un BucketS3.  Del mismo modo, para raelizar el web scrapping se debe leer el archivo obteniendo el contenido en formato html. El nombre del archivo contine la fecha de ejecución del lambda.



Despues de digitar el comando 
En el archivo zappa_settings.json se especifica el nombre del archivo python y la función. Al igual se esteblece que todos los lunes a las 10am se active la función lambda. nicialmente establecia la edxpresión de la sigyuinete manera:

En el momento de validar el hisotria de regsitros en CloudWatch se evidenciaba que no se ejecutaba la función. Despues de varias pruebas e investigandoi en la doucmnetacipón de amazon, encontre que el serrvicio lambda viene de manera predetermnianda con el uso de la zona horaria UTC, comunmnete utilizada en varias partes del mundo. Esta era la razon de porque no se ejecutaba a la hora especificada en la función cron, despues de validar que existen 5 horas de diferencia, modifique el evento para que se ejecutara a las 13 horas, es decir las 10 horas en la zona horaria de bogotá (UTC-5).

A continuación se muestra captura de pantalla del ambiente cloud9, el hsitoria de grsitros de cloudwatch, el almacenmiento de la pagian en el primer bucket y la subida de un archvio csv en el segundo bucket. 

Se realizan varias preubas para que finalmente se obtenga la siguiiente estriuctura del archvio csv








En el archvio json de nombre zappa_settings se realiza la declaración del nombre de la función lambda, el archivo. En mi caso utilice dos ambientes de trabajo en donde cada uno tuviera la declaración de una función con la zona de despliqyu, bucket de lamacenuamienot, el rol de usuario para obtener los permisos necesarios




Primero se valida cual fue el utimo archvio html subido al primer bucket, esta busqueda se realiza encontrado la diferencia entre la fecha actual y la fecha de subida para archvio que se encuentra el atributo Lastmodified del diccioanrio contents. Posteriormente, se analiza y se encunetra los datos de cada casa a traves de BeautifulSoup que permite encontrar todas las etiquetas de la clase listing listing-card. 

Cada atributo representa una lista que se encuentra contenida en un diccionario, que despues a traves de la libreria de pandas vamos a poder obtener un archivo .csv.

Por ora parte 
Se observa que existe una generalidad en la pagina, ya que en cada etiqueta de clase listing-lising card se tiene como atributos, la cantidad de baños, habitaciones y precio. Para cada casa, en algunas ocasiones no se especifica la cantidad de baños o abitaciones, es por esto que primero se realiza una validación en donde si no se espcifica la cantidad se ingresa un valor nulo a la lista.



_Acá va un párrafo que describa lo que es el proyecto_

## Expresión Cron - Agendar evento 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Web scraping - Extracción de datos 📋

### Web scraping - Configuración del archvio zappa_settings 📋

```
zappa init
```

```
zappa deploy dev
```
```
zappa update dev
```

```
zappa schedule dev
```

```
flake8 .
```

Se encarga de


### Pruebas unitarias 🔧
1. Se simula la descarga de una página web utilizando la biblioteca urllib.request y se valida el contenido HTML descargado.
2. Se hace una prueba para validar si el nombre de dominio se encunetra asocidao a una dirección ip que permite saber en que lugar del mundo se encuentra ubicado el servidor

omo entrada y devuelve True si el nombre de host se puede resolver a una dirección IP utilizando socket.

3. Se realiza la petición de tipo GET a la pagina de mitula y se recibe el un codigo que encuentra en el encabezado del mensaje que permite validar si existieron problemas de comunicación desde la parte del cliente o del servidor

4. Se obtiene un archivo html a partir de la url de la pagina de Mitula devuelve el status code 200 si se sube correctamente a un bucket de s3. Para esto se analiza la meta data de la respuesta. La solicitud es satisfactoria y sin erorres cuando se recibe un 200 como respuesta. 

```
def validate_code(url):
    return urllib.request.urlopen(url).getcode()

```







### Revisión de codigo limpio🔧
La libreria flake8 permite examinar los archvios especilamnete de lenugaje python con el fin de advertir errores de sintaxis,redundancia de codigo, el nivel de complejidad de las funciones,variables o impoertaciones no utilizadas durante el desarrollo del cdogio. Se crea un archvio de configuración perosnaliazdo en donde se decide que tipo de reglas aplicar.
```
flake8 --config=.flake8
```




_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
![Texto alternativo](https://i.postimg.cc/0NBSbdCT/Captura-de-pantalla-2023-03-12-234133.png)
![Texto alternativo](https://i.postimg.cc/yY1NC3mc/Captura-de-pantalla-2023-03-12-233732.png)
![Texto alternativo](https://i.postimg.cc/0NBSbdCT/Captura-de-pantalla-2023-03-12-234133.png)
![Texto alternativo](https://i.postimg.cc/0NBSbdCT/Captura-de-pantalla-2023-03-12-234133.png)
![Texto alternativo](https://i.postimg.cc/0NBSbdCT/Captura-de-pantalla-2023-03-12-234133.png)

