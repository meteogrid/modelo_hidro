==================
modelo_hidro v0.1
==================

Version inicial del modelo hidrologico, con uso de vistas html para la representacion y calculo de datos.

Quick start
-----------

1. Add "myblog" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'modelo_hidro'
    'drf_yasg',
    'rest_framework'	
  }

2. Include the myblog URLconf in urls.py:
  url(r'^modelo/', include('modelo.urls')),
  path('api-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

3. Ejecutar 'python3 manage.py migrate' para crear el modelo.

4. Ejecutar y acceder http://127.0.0.1:8000/admin/ para vistas basicas de administracion de tablas.

5. Acceder http://127.0.0.1:8000/modelo/load/ para acceder a la pantalla de carga de datos.

6. Acceder http://127.0.0.1:8000/api-doc/ modelo de documentacion para las APIs.
