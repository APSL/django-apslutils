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

Añadir la aplicación al *settings.py*

<pre>
    INSTALLED_APPS = (
        ...
        'apslutils',
        ...
    )
</pre>

Utilidades
==========

Descripción de las utilidades disponibles, separadas por ficheros.

apslutils.fechas
----------------

**daterange(start_date, end_date)**

Permite hacer una interación entre dos fechas


apslutils.forms
---------------

**EntreFechasField()**

Campo para formularios. Muestra dos fechas. Fecha desde y fecha hasta.

**BootstrapMixin()**

Mixin para formularios. Coloca la clase form-control a todos los campos para
tener compatibilidad con Bootstrap


apslutils.admin
---------------

**ComboBoxFiltro()**

Filtro para la administración. Substituye el típico filtro de lista por un
combobox (select). Útil para FK muy extensos. 

Añadir al *list_filter* con el siguiente formato:

<pre>
    list_filter = ('campo1', 'campo2', ('campo3', ComboBoxFiltro), )
</pre>
