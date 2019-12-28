from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions
from .forms import UserForm


class HelloApiView(APIView):
    """test api view"""
    serializer_class=serializers.HelloSerializer

    def get(self ,request ,format=None):
        """returns a list of APIVIEW feature"""
        an_apiview =[
            'Uses HTTP methods as function (get , post ,put patch ,delete )',
            'It is similar to a traditional Django view ',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]
        return Response({'message': 'hello' ,'an_apiview ': an_apiview})
    def post(self ,request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name= serializer.data.get('name')
            message= 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def put(self,request ,pk=None):
        """Handles updating an object ."""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request , only updates fields provided in the request ."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})

##################################################################

class HelloViewSet(viewsets.ViewSet):
    """Test API Views ."""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
                 """Return a hello message"""
                 a_viewset = [
                      'Uses actions (list , create ,retrieve ,update , partial_update )',
                      'Automatically maps to URLs using Routers ',
                      'provides mor functionality with less code .',
                               ]

                 return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self , request):
                """Create a new hello message ."""
                serializer = serializers.HelloSerializer(data=request.data)
                if serializer.is_valid():
                    name=serializer.data.get('name')
                    message= 'Hello {0}'.format(name)
                    return Response({'message': message})
                else:
                    return Response(
                        serializer.errors , status =status.HTTP_400_BAD_REQUEST)

    def retrieve(self ,request , pk=None):
              """Handles getting an object by its ID ."""
              return Response({'http_method': 'Get'})



    def update(self , request ,pk=None ):

                 """Handles updating an object ."""
                 return Response({'http_method': 'PUT'})


    def partial_update(self , request , pk=None):
        """Handles updating part of an object ."""


        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
         """Handles removing an object ."""

         return Response({'http_method': 'DELETE'})

##############################################################################
class UserProfileViewSet(viewsets.ModelViewSet):
      """Handles creating and updating profiles"""
      serializer_class=serializers.UserProfileSerializer
      queryset = models.UserProfile.objects.all()
      authenticate_classes = (TokenAuthentication,)
      permission_classes = (permissions.UpdateOwnProfile,)
      filter_backends = (filters.SearchFilter,)
      search_fields = ('name' , 'email' ,'label')


class LoginViewSet(viewsets.ViewSet) :
    """Checks email and password and returns an auth token."""
    serializer_class = AuthTokenSerializer


    def create(self , request):
       """Use the ObtainAuthToken APIView to validate and create a token"""

       return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
     """Handles ccreating , reading and updating profile feed items ."""

     authentication_classes = (TokenAuthentication,)
     serializer_class = serializers.ProfileFeedItemSerializer
     queryset = models.ProfileFeedItem.objects.all()
     permission_classes = (permissions.PostOwnStatus , IsAuthenticated)

     def perform_create(self, serializer):
         """Sets the user profile to the logged in user"""

         serializer.save(user_profile=self.request.user)

#class general (viewsets.ModelViewSet):

#   def index(request):
 #       return render(request , 'scolarite/index.html')
#class EtudiantForm (viewsets.ModelViewSet):
 #  def Et_page(request):
  #     return render(request , 'scolarite/Et_page.html')
#class EnseignantForm(viewsets.ModelViewSet) :

 #  def En_page(request):
 #      return render(request , 'scolarite/En_page.html')

#class ChargeForm(viewsets.ModelViewSet):
#   def Ch_page(request):
 #      return render(request , 'scolarite/Ch_page.html')
##################

#def inscrire(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)


   #     if form.is_valid():
    #        form.save()
     #       username = form.cleaned_data['username']
      #      password = form.cleaned_data['password1']
       #     email = form.cleaned_data['email']
        #    user =authenticate(username=username , password=password , email=email)
         #   login(request , user)

          #  return redirect ('index')#redirect in etudiant or enseignant
    #else:
     #  form= UserCreationForm()

    #context={'form' : form}
    #return render(request, 'registration/inscrire.html', context)


