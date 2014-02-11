django-apslutils
================

Herramientas y librerías varias que utiliza el equipo de APSL para sus proyectos

Requerimientos
==============

Ninguno

Instalación
===========

A través de _pip_:

<pre>
pip install git+https://github.com/APSL/django-apslutils.git
</pre>

Añadir al fichero de requerimientos en modo desarrollador:

<pre>
-e git+https://github.com/APSL/django-apslutils.git#egg=apslutils
</pre>

Utilidades
==========

Descripción de las utilidades disponibles, separadas por ficheros.

apslutils.fechas
----------------

**str_to_datetime(fecha, hora)**

Recibe una fecha con formato yyyy-mm-dd, y una hora con formato hh:mm y devuelve un objeto datetime

**daterange(start_date, end_date)**

Permite hacer una interación entre dos fechas

**datetime_to_date(fecha)**

Recibe un objeto datetime.datetime y devuelve un datetime.date

**str_to_date(fecha, formato=1)**

Recibe una cadena en formato fecha y devuelve un datetime.date. 

    formato 1: dd/mm/yyy
    formato 2: yyyy-mm-dd

**str_to_time(hora)**

Data una hora en formato string, devolvemos un datetime.time

    formato: HH:MM
