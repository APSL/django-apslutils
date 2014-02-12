#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------
from django import forms


class EntreFechasWidget(forms.MultiWidget):

    def __init__(self, widgets=None, *args, **kwargs):
        widgets = [forms.DateInput, forms.DateInput]

        super(EntreFechasWidget, self).__init__(widgets=widgets,
            *args, **kwargs)

    def decompress(self, value):
        return [None, None]


class EntreFechasField(forms.MultiValueField):
    u"""
    Campo formado por dos fechas. Fecha desde y
    fecha hasta.
    """

    def __init__(self, *args, **kwargs):

        fields = [forms.DateField(), forms.DateField()]
        widget = EntreFechasWidget()

        super(EntreFechasField, self).__init__(fields, widget=widget,
            *args, **kwargs)

    def compress(self, data_list):
        return { 'desde': data_list[0], 'hasta': data_list[1] }
