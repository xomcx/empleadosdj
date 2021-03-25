from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos las urls de la app departamento
    re_path('',include('applications.departamento.urls')),
    #incluimos las urls de la app persona
    re_path('',include('applications.persona.urls')),
    #incluimos las urls de la app home
    re_path('',include('applications.home.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
