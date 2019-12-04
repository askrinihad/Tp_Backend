from django.conf.urls import include , url
from django.contrib import admin
urlpatterns = [

    url(r'^admin/',admin.site.urls),
    url(r'^scolarite/', include('scolarite.urls')),
    url(r'^api/',include('scolarite.urls')),
    url(r'^inscrire/', include('scolarite.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]
#from django.contrib import admin
#from django.urls import include , path
#urlpatterns = [
 #   path('scolarite/', include('scolarite.urls')) ,
  #  path('admin/', admin.site.urls),
#]
