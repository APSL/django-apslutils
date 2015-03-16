#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

import datetime

from django.contrib import admin
from django.db.models.fields import DateTimeField
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _


class ComboBoxFiltro(admin.RelatedFieldListFilter):
    u"""
    Mostramos otra plantilla para los filtros de tipo lista que tienen
    muchos ítems
    """
    template = 'admin/combofiltro.html'


class ComboBoxCharFiltro(admin.AllValuesFieldListFilter):
    u"""
    Parecibo al ComboBoxFiltro, pero este es para campos de tipo CharField.
    ComboBoxFiltro herea de RelateField... y deben ser campos de tipo FK
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

    def __init__(self, request, params, model, model_admin):
        super(RangoFechasFiltro, self).__init__(request, params, model, model_admin)
        self.model = model

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

            try:
                desde = self._get_date(desde, inicio=True)
                hasta = self._get_date(hasta, inicio=False)
            except ValueError:
                pass
            else:
                args = {
                    '%s__gte' % self.value(): desde,
                    '%s__lte' % self.value(): hasta
                }
                queryset = queryset.filter(**args)

        return queryset

    def _get_date(self, fecha, inicio=True):
        """Devuelve datetime.date o datetime.datetime segun el atributo del modelo"""
        _fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y')
        model_field = self.model._meta._name_map[self.value()][0]
        if isinstance(model_field, DateTimeField):
            if inicio:
                return _fecha.replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                return _fecha.replace(hour=23, minute=59, second=59, microsecond=999999)
        else:
            return _fecha.date()


class MultiSelectorFiltro(admin.SimpleListFilter):
    u"""
    Filtro multiselector.
    Cada elemento del selector esta formado por una clave obtenida a
    partir de 'filter_by' y por un nombre obtenido a partir de 'parameter_name'.
    El listado de valores del filtro viene delimitador por '|'.
    """

    title = u'Por Nombre'
    parameter_name = 'name'
    template = 'admin/multiselector.html'
    filter_by = 'code'

    def lookups(self, request, model_admin):
        return ((getattr(obj, self.filter_by, ''), getattr(obj, self.parameter_name, '')) for obj in model_admin.model.objects.all())

    def queryset(self, request, queryset):
        filter_args = request.GET.get(self.parameter_name)

        if filter_args:
            codes = filter_args.split('|')
            kwargs = {
                "{}__in".format(self.filter_by): codes
            }
            queryset = queryset.filter(**kwargs)

        return queryset

    def choices(self, cl):
        args = self.value().split("|") if self.value() else []
        yield {
            'selected': self.value() is None,
            'query_string': cl.get_query_string({}, [self.parameter_name]),
            'display': _('All'),
        }
        for lookup, title in self.lookup_choices:
                yield {
                    'selected': force_text(lookup) in args,
                    'query_string': cl.get_query_string({
                        self.parameter_name: lookup,
                    }, []),
                    'display': title,
                }
