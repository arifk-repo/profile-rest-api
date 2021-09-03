from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
