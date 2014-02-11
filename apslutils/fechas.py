#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------
import datetime

from django.utils.translation import ugettext as _


def str_to_datetime(fecha, hora):
    u"""
        - fecha: string con formato: yyyy-mm-dd
        - hora: string con formato: hh:mm
    """

    try:
        anyo, mes, dia = fecha.split('-')
    except ValueError:
        return

    try:
        hora, minutos = hora.split(':')
    except ValueError:
        return

    try:
        return datetime.datetime(int(anyo), int(mes), int(dia),
                                 int(hora), int(minutos), 00)
    except (TypeError, ValueError):
        return


def daterange(start_date, end_date):
    u"""
    Permite iterar dos fechas
    """
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + datetime.timedelta(n)


def datetime_to_date(fecha):
    return datetime.date(fecha.year, fecha.month, fecha.day)


def str_to_date(fecha, formato=1):
    u"""Recibimos una fecha en str y devolvemos un objeto date.

        formato 1: dd/mm/yyy
        formato 2: yyyy-mm-dd
    """

    try:
        if formato == 1:
            dia, mes, anyo = fecha.split('/')
        elif formato == 2:
            anyo, mes, dia = fecha.split('-')
    except ValueError:
        return

    try:
        return datetime.date(int(anyo), int(mes), int(dia))
    except (TypeError, ValueError):
        return


def str_to_time(hora):
    u"""
    Recibimos una hora en formato HH:MM y devolvemos un time
    """
    
    hora, minutos = hora.split(':')
    hora, minutos = int(hora), int(minutos)

    return datetime.time(hora, minutos)
