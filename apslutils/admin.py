#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

import datetime

from django.contrib import admin


class ComboBoxFiltro(admin.RelatedFieldListFilter):
    u"""
    Mostramos otra plantilla para los filtros de tipo lista que tienen
    muchos ítems
    """
    template = 'admin/combofiltro.html'


class RangoFechasFiltro(admin.SimpleListFilter):
    u"""
    Filtro para rangos de fechas. Además se puede escoger entre distintos
    campos del modelo. Por ejemplo filtrar por fecha de creación o 
    fecha de modificación.
    """

    title = u'Por fechas'
    parameter_name = 'flt_fechas'
    template = 'admin/porfechasfiltro.html'

    # Tipos de filtraje
    filtro_tipos = ()

    def value(self):
        valor = self.used_parameters.get(self.parameter_name, None)
        if valor:
            valor = valor.split('|')[0]

        return valor

    def lookups(self, request, model_admin):
        return self.filtro_tipos

    def queryset(self, request, queryset):

        filtro = request.GET.get(self.parameter_name)
        if filtro:
            desde, hasta = filtro.split('|')[1:]
            desde = datetime.datetime.strptime(desde, '%d/%m/%Y').date()
            hasta = datetime.datetime.strptime(hasta, '%d/%m/%Y').date()

            args = {
                '%s__gte' % self.value(): desde,
                '%s__lte' % self.value(): hasta
            }
            queryset = queryset.filter(**args)

        return queryset