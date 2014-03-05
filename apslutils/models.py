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
