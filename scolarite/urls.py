from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter


from . import views
from .forms import UserForm

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet , base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login' , views.LoginViewSet , base_name='login')
router.register('feed' , views.UserProfileFeedViewSet)

urlpatterns = [

  #url(r'^$', views.general ,name='index'),
   #url(r'^$', views.general ,name='Et_page'),

  url(r'^hello-view/',views.HelloApiView.as_view()),
  url(r'' , include(router.urls)),


  #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form':  UserForm}),
 #url(r'^inscrire/$', views.inscrire.as_view(), name='inscrire'),

 #url(r'inscrire^$', views.UserFormView.as_view(), name='inscrire'),

]
#from django.urls import path
#from . import views
#urlpatterns = [
 #   path('',views.index , name='index') ,

#]