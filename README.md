* Universidad Sergio Arboleda
* Big Data
* Parcial 3° corte
* Domingo 12 de marzo de 2023
## Ejecución de la función lambda para la descarga del archivo .html
Se describe el proceso realizado para hacer web scraping a la página de Mitula. Por un lado, se configura un evento a las 10 am de cada lunes, con el fin de que se realice un trigger hacia la función lambda y se ejecute la función f, escrita en lenguaje Python. Esta función tiene un desencadenador hacia un bucket s3 que permite guardar la página en una carpeta llamada landing-casas-xxx. Del mismo modo, para realizar el web scraping se debe leer el archivo obteniendo el contenido en formato html almacenado en el primer bucket.

Después de digitar el comando, en el archivo zappa_settings.json se especifica el nombre del archivo Python y la función. Asimismo, se establece que todos los lunes a las 9 am se active la función lambda. Inicialmente se establecía la expresión de la siguiente manera: cron(0 9 ? '*' MON '*'). En el momento de validar el historial de registros en CloudWatch se evidenciaba que no se ejecutaba la función. Después de varias pruebas e investigando en la documentación de Amazon, encontré que el servicio lambda viene de manera predeterminada con el uso de la zona horaria UTC, comúnmente utilizada en varias partes del mundo. Esta era la razón de por qué no se ejecutaba a la hora especificada en la función cron. Después de validar que existen 5 horas de diferencia, modifiqué el evento para que se ejecutara a las 13 horas, es decir, las 10 horas en la zona horaria de Bogotá (UTC-5).

![Texto alternativo](https://i.postimg.cc/bJfzCZYG/Captura-de-pantalla-2023-03-12-231529.png)

A continuación, se muestra una captura de pantalla de la subida de la página al primer bucket y la subida de un archivo CSV en el segundo bucket.

![Texto alternativo](https://i.postimg.cc/g25chMfH/Captura-de-pantalla-2023-03-12-232012.png)

![Texto alternativo](https://i.postimg.cc/K84vRXsY/Captura-de-pantalla-2023-03-12-231937.png)

Se realizaron varias pruebas para que finalmente se obtuviera la siguiente estructura del archivo CSV:

![Texto alternativo](https://i.postimg.cc/yNZ1ymK4/Captura-de-pantalla-2023-03-12-233355.png)


En el archivo JSON de nombre zappa_settings se realiza la declaración del nombre de la función lambda y el archivo. En mi caso, utilicé dos ambientes de trabajo en donde cada uno tuviera la declaración de una función con la zona de despliegue, bucket de almacenamiento y el rol de usuario para obtener los permisos necesarios.

Primero se valida cuál fue el último archivo HTML subido al primer bucket. Esta búsqueda se realiza encontrando la diferencia entre la fecha actual y la fecha de subida para archivo que se encuentra el atributo Lastmodified del diccionario contents. Posteriormente, se analiza y se encuentra los datos de cada casa a través de BeautifulSoup que permite encontrar todas las etiquetas de la clase listing listing-card.

Cada atributo representa una lista que se encuentra contenida en un diccionario, que después a través de la librería de Pandas vamos a poder obtener un archivo .csv.

Por otra parte, se observa que existe una generalidad en la página, ya que en cada etiqueta de clase listing-lising card se tiene como atributos, la cantidad de baños, habitaciones y precio. Para cada casa, en algunas ocasiones no se especifica la cantidad de baños o habitaciones, es por esto que primero se realiza una validación en donde si no se especifica la cantidad se ingresa un valor nulo a la lista.


_Acá va un párrafo que describa lo que es el proyecto_

### Expresión Cron - Agendar evento 🚀

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

* [Zappa] - Despliegue
* [pytest] - Ejecución de pruebas
* [flake8] - Usado para generar RSS


---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
![Texto alternativo](https://i.postimg.cc/0NBSbdCT/Captura-de-pantalla-2023-03-12-234133.png)
![Texto alternativo](https://i.postimg.cc/yY1NC3mc/Captura-de-pantalla-2023-03-12-233732.png)
![Texto alternativo](https://i.postimg.cc/yNZ1ymK4/Captura-de-pantalla-2023-03-12-233355.png)
![Texto alternativo](https://i.postimg.cc/g25chMfH/Captura-de-pantalla-2023-03-12-232012.png)
![Texto alternativo](https://i.postimg.cc/K84vRXsY/Captura-de-pantalla-2023-03-12-231937.png)
![Texto alternativo](https://i.postimg.cc/bJfzCZYG/Captura-de-pantalla-2023-03-12-231529.png)
![Texto alternativo](https://i.postimg.cc/6qkLysd4/Captura-de-pantalla-2023-03-13-022143.png)
