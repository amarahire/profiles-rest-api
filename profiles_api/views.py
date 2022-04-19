from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):

    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of api features"""

        an_apiview = [
        "Uses HTTP methods as function (get,post,put,patch,delete)",
        "Is similar to a traditional django view",
        "Gives you the most control over your application logic",
        "Is mapped manually to URLs"
        ]

        return Response({'message':'helloapi',"apiview":an_apiview})
