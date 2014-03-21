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

**ComboBoxCharFiltro**

Igual que el filtro ComboBoxFiltro pero para campos que no sean de tipo
ForeignKey. 

**RangoFechasFiltro()**

Filtro para fechas desde y hasta. Además se muestra un combo para seleccionar
sobre qué campo (tipo fecha) queremos aplicar el filtro.

Por ejemplo por si queremos filtrar por fecha desde y hasta de creación, o
o fecha de recogida.

Uso:

Importación:

<pre>
from apslutils.admin import RangoFechasFiltro
</pre>

Creamos un nuevo objeto heredando del filtro
<pre>
class FiltroReservaOld(RangoFechasFiltro):
    filtro_tipos = (
        ('fecha_reserva', u'Fecha de reserva'),
        ('fecha_recogida', u'Fecha de recogida'),
    )
</pre>

Y usamos
<pre>
list_filter = ('estado', FiltroReservaOld, 'asociado', )
</pre>

apslutils.models
----------------

**subir_archivo(carpeta, fichero)**

Método para ser utilizado en atributos upload_to de fields de tipo ImageField,
FileField.

Permite una mejora organización de ficheros subidos, guardándolos en carpetas
por fechas y haciendo slugify del nombre.

En el modelo:

<pre>
from apslutils.models import subir_archivo
        
def img_finca(objeto, filename):
    return subir_archivo('finca', filename)

imagen = models.ImageField(upload_to=img_finca)
</pre>

Templatetags
============

lista_errores
-------------

Recibe un formulario, y si no es válido, expulsa una lista de errores
formatado para Bootstrap 3.

Uso dentro del template:
<pre>
    {% load apslutils %}
    {% lista_errores form %}
</pre>

Static
======

En static se encuentran recursos comunes, como pueden ser plugins de jquery

Javascripts
-----------

jquery.i18nfields
-----------------

Plugin para modeltranslation. El resultado es parecido al que modeltranslation efectua
dentro del admin de django, agrupando los campos traducibles en pestañas y
añadiendo arriba un combo de cambio de idioma general.

Este plugin es compatible con bootstrap3 y se puede añadir en cualquier template donde
haya un formulario. 

Modo de uso:

<pre>
    Importar script: "{{STATIC_URL}}apslutils/js/jquery.i18nfields.js"
    
    $(function() {
        $('form').i18nfields({idioma_defecto: '{{LANGUAGE_CODE}}'});
    });    
</pre>

jquery.slugify
--------------

Plugin para hacer un slugify en tiempo real. Por defecto lo hace del campo nombre
hacia el slug.

Modo de uso:

<pre>
    Importar script: "{{STATIC_URL}}apslutils/js/jquery.slugify.js"
    
    $(function() {
        $('form').slugify();
    });  
</pre>
