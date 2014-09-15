#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------
from django import forms
from django.template.loader import render_to_string


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


class BootstrapMixin(forms.Form):
    u"""
    Añade la clase form-control a todos los inputs para compatibilidad
    con bootstrap    
    """

    def __init__(self, *args, **kwargs):
        super(BootstrapMixin, self).__init__(*args, **kwargs)

        for f in self.fields.values():
            if isinstance(f, forms.BooleanField):
                continue

            if 'class' in f.widget.attrs:
                f.widget.attrs['class'] += ' form-control'
            else:
                f.widget.attrs['class'] = 'form-control'


# Si tenemos crispy_forms instalado, definimos un nuevo MultiField compatible
# con bootstrap3.

try:
    from crispy_forms.layout import MultiField
except ImportError:
    pass
else:
    from crispy_forms.layout import TEMPLATE_PACK, Field
    
    class MultiFieldBootstrap(MultiField):
        def __init__(self, label, *fields, **kwargs):
            super(MultiFieldBootstrap, self).__init__(label, *fields, **kwargs)
            self.template = "apslutils/crispy/multifieldbs.html"
            
        def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
            requerido, hay_error = False, False
            
            campos = []
            for campo in self.fields:
                nombre_campo = campo.fields[0] if isinstance(campo, Field) else campo
                form_campo = form[nombre_campo]

                if isinstance(campo, Field):
                    form_campo.field.widget.attrs.update(campo.attrs)
                
                campos.append(form_campo)

                if form_campo.field.required: requerido = True
                if form_campo.errors: hay_error = True
                
            context.update({"multifield": self, "fields_list": campos,
                            "is_required": requerido, "has_error": hay_error})
            
            return render_to_string(self.template, context)

####################################
# Formularios y campos para Metro Ui

class MetroForm(object):
    u"""
    Configuración para los formulario que usan Metro UI.
    """

    # Atributos de configuración por defecto
    metro_action = "."
    metro_method = "post"
    metro_submit_value = u"Submit"
    metro_style = "default"  # Posibles: default | inline
    metro_show_errors = True

    # Atributos internos


    def __init__(self, *args, **kwargs):
        super(MetroForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.metro_role = "input-control"
            
            if isinstance(field.widget, forms.Select):
                field.widget.input_type = "select"

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.input_type = "checkbox"

            if isinstance(field, forms.DateField):
                field.metro_role = "datepicker"
                
            if field.label:
                field.widget.attrs["placeholder"] = field.label

        
class MetroDateField(forms.DateField):
    metro_locale = "en"
    metro_format = "dd/mm/yyyy"

    
