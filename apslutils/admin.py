#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from django.contrib import admin


class ComboBoxFiltro(admin.RelatedFieldListFilter):
    u"""
    Mostramos otra plantilla para los filtros de tipo lista que tienen
    muchos ítems
    """
    template = 'admin/combofiltro.html'
