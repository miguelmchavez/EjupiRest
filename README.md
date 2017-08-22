# Ejupi Rest
> API Rest para acceder a información del Servicio de Transporte Público de Encarnación.



Ejupi Rest es un proyecto que pretender brindar información acerca del Servicio de Transporte Público de Encarnación.
La API está hecha en Django, el proyecto cuenta además con una aplicación que consume la información disponible de manera que sea más fácil para el público acceder a ella.


![](../header.png)

## Requerimientos

### Requerimientos principales
* Python 
* PostgreSQL 
* Django 

### Otras Librerías
`django-filter`

`djangorestframework`

`psycopg2`

`django-cors-headers`


## Instrucciones


```
git clone git@github.com:miguelmchavez/ejupirest.git
cd ejupirest
virtualenv env
source env/bin/activate 
pip install -r requerimientos.txt

## Puntos de Acceso
A pesar de que el servicio se encuentra en línea, la cantidad de datos disponible es incompleta. 
A través de los siguientes puntos de acceso se puede encontrar la información disponible:

* http://www.ejupi.co/api/v1/recorrido/
* http://www.ejupi.co/api/v1/detallerecorrido/
* http://www.ejupi.co/api/v1/parada/



