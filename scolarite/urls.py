from django.conf.urls import url
from . import views


urlpatterns = [

  url(r'^$', views.index ,name='index'),
  url(r'^hello-view/',views.HelloApiView.as_view()),
 #url(r'^inscrire/$', views.inscrire.as_view(), name='inscrire'),

 #url(r'inscrire^$', views.UserFormView.as_view(), name='inscrire'),

]
#from django.urls import path
#from . import views
#urlpatterns = [
 #   path('',views.index , name='index') ,

#]