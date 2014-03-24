/*
File: jquery.slugify.min.js

Transforma a slug un campo

Modo de uso:
    <script src="{{STATIC_URL}}apslutils/js/jquery.slugify.js"></script>
    
    $(function() {
        $('form').slugify();
    });  
*/
( function($) {
    var _self;
    var _options;
    var _campos_slug;

    $.fn.slugify = function(options, args) {
        _self = this;
    
        if (typeof(options) == 'string') {
            return eval(options)(args);
        } else {
            _options_default = {
                campo_origen: 'nombre',
                campo_slug: 'slug'
            };
            _options = jQuery.extend(_options_default , options);
            init();
        }
    };
    
    function init() {
        _campos_slug = $(_self).find('input[id^="id_'+_options.campo_origen+'_"]');
        
        $(_campos_slug).each(function(indx, campo) {
            var idioma = $(campo).prop('id').split('_').slice('-1')[0];
            $(campo).keyup(function() {
                var valor = $(this).val();
                var slug = URLify(valor);
                $('input[name="'+_options.campo_slug+'_'+idioma+'"]').val(slug).trigger('change');
                
                
            });
        });
    }

})(jQuery);
