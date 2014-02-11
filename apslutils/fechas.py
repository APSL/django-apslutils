#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------
import datetime


def daterange(start_date, end_date):
    u"""
    Permite iterar dos fechas
    """
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + datetime.timedelta(n)

