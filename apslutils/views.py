#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

try:
    import django_filters
    import crispy_forms
    
    from django_tables2 import SingleTableView, RequestConfig
except ImportError:
    class TablaFiltradaView(object):
        raise Exception(u"Es necesario django-tables2, django-filter y django-crispy-forms")
else:
    class TablaFiltradaView(SingleTableView):
        u"""
        Vista genérica para utilizar filtros y tablas de django_tables2 y
        django_filters. Todo controlado en una sola vista.
        También utiliza django_crispy_forms par dibujar los filtros.
        """

        filter_class = None
        formhelper_class = None

        def get_queryset(self, **kwargs):
            qs = super(TablaFiltradaView, self).get_queryset()

            if self.filter_class:
                self.filter = self.filter_class(self.request.GET, queryset=qs)
                self.filter.form.helper = self.formhelper_class() \
                                          if self.formhelper_class else None
                return self.filter.qs

            return qs
            
        def get_table(self, **kwargs):
            table = super(TablaFiltradaView, self).get_table()
            page = self.kwargs.get("page", 1)
            
            RequestConfig(self.request,
                          paginate={"page": page,
                                    "per_page": self.paginate_by}).configure(table)
            return table
            
        def get_context_data(self, **kwargs):
            ctx = super(TablaFiltradaView, self).get_context_data()

            if hasattr(self, "filter"):
                ctx["filter"] = self.filter
                
            return ctx
