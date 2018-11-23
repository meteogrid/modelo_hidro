from django.conf.urls import url

from modelo import views

urlpatterns = [
    url(r'^data/$', views.CalculoModeloListView.as_view(), name='modelo_datos'),
    url(r'^calculo_data/$', views.get_calculo_data, name='get_calculo_data'),
    url(r'^get_unidades/$', views.load_unidad_hidro, name='get_unidades'),
    url(r'^load/$', views.load_file_view, name='load_file'),
    url(r'^load_data/$', views.load_data_file, name='load_data_file'),
    url(r'^create_data/$', views.create_data, name='create_data')
]