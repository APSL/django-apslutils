/*
File: jquery.i18nfields.min.js

Plugin para campos de modeltranslation. Los transforma en tabs compatibles
con bootstrap 3.

Modo de uso:
    <script src="{{STATIC_URL}}apslutils/js/jquery.i18nfields.js"></script>
    
    $(function() {
        $('form').i18nfields({idioma_defecto: '{{LANGUAGE_CODE}}'});
    });    

*/
( function($) {
    var _self;
    var _options;
    var _campos_i18n;

    $.fn.i18nfields = function(options, args) {
        _self = this;
        _campos_i18n = $(_self).find('.i18nfield');
    
        if (typeof(options) == 'string') {
            return eval(options)(args);
        } else {
            _options_default = {
                selector_contenedor: '.form-group',
                id_selector_idioma: 'selector-global-idioma'
            };
            _options = jQuery.extend(_options_default , options);
            init();
        }
    };
    
    // Recorremos cada campo, construimos los tabs y los añadimos en el dom
    function init() {
        $(_campos_i18n).each(function(indx, campo) {

            var nombre = $(campo).attr('id');
            var label = $(campo).closest(_options.selector_contenedor)
                                .find('label').text();
            var idiomas = get_idiomas(campo, nombre);
            selector_idiomas_global(idiomas);
            var campo_contenedor = $(campo).closest(_options.selector_contenedor);
            
            // Ocultamos el campo, sin el idioma. Los campos con idioma ya se ocultan en el
            // bucle siguiente...
            $(campo_contenedor).find('label, div').hide();

            // Aquí es donde metemos el ul de las pestañas y los divs del contenido
            // de cada una de ellas
            var contenedor_tabs = $('<div/>').appendTo(campo_contenedor);

            // Ul de las pestañas. Selector de idioma
            var ul = $('<ul/>').addClass('nav nav-tabs').appendTo(contenedor_tabs);

            // Contenido de cada pestaña
            var div = $('<div/>').addClass('tab-content').appendTo(contenedor_tabs);

            // Para cada idioma añadimos un ítem en el ul de navegación de pestañas
            // y un div para su contenido
            $(idiomas).each(function(indx, idioma) {
                // Li para el selector de idiomas
                $('<li/>').appendTo(ul).append(
                    $('<a data-toggle="tab" />')
                        .text(idioma)
                        .data({'nombre': nombre, 'idioma': idioma})
                        .prop('href', '#' + nombre + '_' + idioma)
                        .click(actualiza_cont_idioma_orig)
                );

                // Recuperamos el label y el input del campo con idioma y le
                // sustiuimos el label. Por que por defecto es del tipo
                // "Como llegar [es]"" y lo dejamos en "Como llegar"
                var label_input = $('#' + nombre + '_' + idioma)
                                  .closest(_options.selector_contenedor)
                                  .data('nombre', nombre);
                $(label_input).find('label').text(label);

                // Capa contenedora del tab
                $('<div/>').addClass('tab-pane')
                           .prop('id', nombre + '_' + idioma)
                           .html(label_input)
                           .appendTo(div);

                // Si el idioma es igual al idioma por defecto, debemos añadir un evento
                // que al modificar el input y salir, también modifique el campo base. 
                // Es decir, si se modifica el campo nombre_es, también debemos modificar
                // el campo nombre, a secas.
                if (idioma == _options.idioma_defecto) {
                    $(label_input).find('input, textarea')
                                  .data('nombre', nombre)
                                  .change(function() {

                        var nombre_campo = $(this).data('nombre');
                        console.log(nombre_campo);
                        $('#' + nombre_campo).val($(this).val());
                    });
                }
            });

            // Marcamos los primeros ítems de la navegación y el contenido del
            // tab
            $(ul).find('li:first').addClass('active');
            $(div).find('div:first').addClass('active');
        });
    }

    // Del campo facilitado, devolvemos una lista de sus idiomas
    function get_idiomas(campo, nombre) {
        var idiomas = [];

        $('[id^='+nombre+']').each(function(indx, campo) {
            var idioma = $(campo).attr('id').split('_').slice(-1)[0];
            if (idioma.length == 2) idiomas.push(idioma);
        });

        return idiomas;
    }

    // Se ejecuta al hacer click sobre una pestaña. Cogemos el contenido del
    // idioma original y lo actualizamos debajo del campo que estamos editando.
    // Así, si estamos en EN, podemos ver lo que pone en el odioma ES si tener
    // que cambiar de pestaña
    function actualiza_cont_idioma_orig() {
        var idioma = $(this).data('idioma');

        if (idioma != _options.idioma_defecto) {
            var nombre_origen = $(this).data('nombre') + '_' + _options.idioma_defecto;
            var nombre_destino = $(this).data('nombre') + '_' + idioma;
            var valor_orig = $('input#' + nombre_origen + ', textarea#' + nombre_origen).val();

            var dest = $('#div_' + nombre_destino).find('div.well');
            if ($(dest).length == 0) {
                $('<br/>').css('clear', 'both').appendTo($('#div_' + nombre_destino));

                dest = $('<div/>', {'class': 'well'}).css({
                    'padding': '0.5em',
                    'font-size': '10px',
                    'width': '96%',
                    'margin': '1em auto 0 auto'
                }).appendTo($('#div_' + nombre_destino));
            }
            $(dest).text(valor_orig);    
        }
    }

    // Si aún no se ha añadido el selector global de idioma, para poder cambiar
    // todas las pestañas de golpe, lo añadimos
    function selector_idiomas_global(idiomas) {
        // Primero comprobamos si está...
        if($('body').find('#' + _options.id_selector_idioma).length == 0) {
            
            // Estilos de la capa
            var css = {
                'position': 'fixed',
                'top': '140px',
                'right': '-78px',
                'width': '115px',
                'z-index':1000,
                'background': '#f0ad4e',
                'border': '1px #eea236 solid',
                'padding': '.2em',
                'cursor': 'pointer',
                'border-radius': '4px 0px 0px 4px'
            };

            // Estilos del select
            var css_select = {
                'display': 'inline-block',
                'width': '70px',
                'margin-left': '.5em'
            };

            // Esilos icono
            var css_icono = {
                'font-size': '35px',
                'vertical-align': '-7px',
                'color': 'white'
            }

            var div = $('<div/>').prop('id', _options.id_selector_idioma)
                                 .css(css).appendTo('body');
            var icon = $('<i class="fa fa-globe"/>')
                            .css(css_icono)
                            .appendTo(div)
                            .click(animacion_idioma);
            
            var select = $('<select/>').prop('class', 'form-control input-sm')
                         .css(css_select)
                         .appendTo(div).change(cambio_idioma);

            $(idiomas).each(function(indx, idioma) {
                $('<option/>').val(idioma).html(idioma).appendTo(select);
            });    
        }   
    }

    // Acción cuando se cambia el idioma del selector de idioma global
    function cambio_idioma() {
        var idioma = $(this).val();
        $('.nav-tabs a[href$="_'+idioma+'"]').trigger('click');
        $('#' + _options.id_selector_idioma).find('i').trigger('click');
    }

    // Animación capa de idioma general
    function animacion_idioma() {
        var estado = $(this).parent().data('estado');
        if (estado == undefined || estado == 'cerrado') {
            $(this).parent().animate({'right': '0px'}, 'fast')
                .data('estado', 'abierto');    
        } else {
            $(this).parent().animate({'right': '-78px'}, 'fast')
               .data('estado', 'cerrado');
        }
    }

})(jQuery);

