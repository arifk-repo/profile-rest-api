from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return a list of APIViews features"""
        an_apiviews=[
            'Uses HTTP method as a function (get,post,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application locig',
            'Is mapped manually to URL'
        ]
        return Response({
            'message':'Hello',
            'an_apiview':an_apiviews
        })