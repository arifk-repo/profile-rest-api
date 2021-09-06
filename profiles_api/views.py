from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializer


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIViews features"""
        an_apiviews = [
            'Uses HTTP method as a function (get,post,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application locig',
            'Is mapped manually to URL'
        ]
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiviews
        })

    def post(self, request):
        """create a hello world with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message': message
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling update an object"""
        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):
        """Handling a partial update of an object"""
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk=None):
        """Handling Delete an Object"""
        return Response({
            'method': 'DELETE'
        })


class HelloViewSet(viewsets.ViewSet):
    """Test API View SET"""

    def list(self, request):
        """Return a Hello message"""
        a_view = [
            'Uses actions (list, create, retrieve,update, partial_message',
            'Automactically maps to URLs using Routers',
            'Provides more functionallity with less code',
        ]
        return Response({
            'message': 'Hello',
            'a_viewset': a_view
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """getting data by id"""
        return Response({'http-method': 'get'})

    def update(self, request, pk=None):
        """updating data by id"""
        return Response({'http-method': 'update'})

    def partial_update(self, request, pk=None):
        """updating part data by id"""
        return Response({'http-method': 'Patch'})

    def destroy(self, request, pk=None):
        """removing data by id"""
        return Response({'http-method': 'delete'})