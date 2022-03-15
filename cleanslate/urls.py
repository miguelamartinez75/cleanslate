from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('objetivos.urls')),
    path('objetivos/', include('objetivos.urls')),    #Lo agregue para poder ver el resumen por puesto
]
