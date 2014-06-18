#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

import os
import datetime

from django.conf import settings
from django.template.defaultfilters import slugify


def subir_archivo(carpeta, fichero):
    u"""
    Método para ser utilizado en el atributo upload_to de los fields tipo
    ImageField, FileField. Ayuda a organizar la carpeta de uploads.

    Modo de uso:

    En el modelo
        from apslutils.models import subir_archivo
        
        def img_finca(objeto, filename):
            return subir_archivo('finca', filename)

        imagen = models.ImageField(upload_to=img_finca)

    """

    ahora = datetime.date.today().strftime('%Y%m')
    uploads = "uploads/{carpeta}/{ahora}/".format(carpeta=carpeta, ahora=ahora)
    path = os.path.join(settings.MEDIA_ROOT, uploads)

    if not os.path.exists(path):
        os.makedirs(path)

    nombre, extension = os.path.splitext(fichero)

    return os.path.join(uploads, slugify(nombre) + extension)


def traspaso_attrs_i18n(modelo_from, campo_from,
                        modelo_to, campo_to):
    u"""
    De un campo origen traspasamos el campo i18n al otro modelo.
    """

    corig = getattr(modelo_from, campo_from)
    cdest = setattr(modelo_to, campo_to, corig)
    
    for lang in settings.LANGUAGES:
        corig = getattr(modelo_from, "{}_{}".format(campo_from, lang[0]))
        setattr(modelo_to, "{}_{}".format(campo_to, lang[0]), corig)
        
