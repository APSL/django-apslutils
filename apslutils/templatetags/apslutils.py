#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------
import datetime

from django import template
from django.utils.translation import ugettext as _


register = template.Library()


@register.tag("lista_errores")
class ListaErroresNode(template.Node):
    u"""
    Recibe un formulario, y si no es válido, expulsa una lista de errores
    formatado para Bootstrap 3.

    Uso dentro del template:
        {% load apslutils %}
        {% lista_errores form %}
    """

    def __init__(self, parser, token):
        self.args = [parser.compile_filter(arg)
            for arg in token.split_contents()[1:]]

    def render(self, ctx):
        form = [arg.resolve(ctx) for arg in self.args][0]
        
        html_errores = []
        html = ''

        for campo, errores in form.errors.items():
            for error in errores:
                campo = ('<strong>%s</strong>: ' % campo if campo != '__all__'
                                                         else '')
                html_errores.append('<li>%s%s</li>' %
                    (campo, error))

        if html_errores:
            html = """
                <div class="alert alert-danger">
                    <span class="glyphicon glyphicon-remove-circle"></span>
                    %(texto)s<br/><br/>
                    <ul class="list-unstyled">%(errores)s</ul>
                </div>""" % {
                    'errores': ' '.join(html_errores),
                    'texto': _(u'Por favor, revisa los errores marcados en rojo.')
                }

        return html


@register.filter
def mod(num, val):
    return num % val == 0
    

@register.filter
def strtodate(fecha_str):
    u"""
    Recibe una fecha en formato: 2014-06-16T12:34:38.874Z y
    devolvemos un objeto datetime
    """

    if not fecha_str:
        return
        
    formatos = ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"]

    for formato in formatos:
        try:
            fecha = datetime.datetime.strptime(fecha_str, formato)
        except ValueError:
            continue
        else:
            return fecha
        
