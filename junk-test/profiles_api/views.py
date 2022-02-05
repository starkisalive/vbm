from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



class HelloAPIView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """returns a list of api view features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, Put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over app logic',
            'mapped manually to urls',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'welcome '+name
            return Response({'message':message})
        return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """handles partial update of an obj"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an obj"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """returns a hello message"""
        a_viewset = [
            'uses actions(create,list,retrive,update, partial update)',
            'automatically maps to url using routers',
            'more functionality with less code',
        ]
        return Response({'message': 'its working', 'a_viewset': a_viewset})


    def create(self, request):
        """creates a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'welcome ' + name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting and obj by its id"""
        return Response({'http method': 'GET'})

    def update(self,request, pk=None):
        """handle updating an obj"""
        return Response({'HTTP method':'PUT'})

    def partial_update(self,request,pk=None):
        """handle updating part of an obj"""
        return Response({
            'HTTP method': 'PATCH'
        })

    def destroy(self,request,pk = None):
        """handle removing an obj"""
        return Response({'HTTP method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating reading and updateing profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


def HomeView(request):
    return render(request, 'home.html')