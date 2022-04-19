from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers import HelloSerializers

class HelloAPIView(APIView):

    serializer_class = HelloSerializers

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


    def post(self,request):

        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'

            return Response({'message':message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handle updating the object"""
        return Response({"method":'PUT'})

    def patch(self, request,pk=None):
        """Handle updating the partial object"""
        return Response({"method":'PATCH'})

    def delete(self,request,pk=None):
        """Deleting an object"""

        return Response({"method":'DELETE'})
