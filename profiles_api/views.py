from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers import HelloSerializers


###### APIView #################
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


###### Viewset #######
from rest_framework import viewsets

class HelloViewsets(viewsets.ViewSet):

    """ Test API Viewset """
    serializer_class = HelloSerializers

    def list(self,request):
        """ Return a hello message """
        a_viewset = [
        'Uses actions (list,create,retrieve,update,partial_update,destroy)',
        'Automatically maps to URLS using routers',
        'Provides more functionality with less code'
        ]

        return Response({"message":"Hello!", 'a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({"message":message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """Handle getting an object by ID"""
        return Response({"message":"RETRIEVE"})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({"message":"UPDATE"})

    def partial_update(self,request,pk=None):
        """Handle partial updating an object"""
        return Response({"message":"PATCH"})

    def destroy(self,request,pk=None):
        """Handle destroying an object"""
        return Response({"message":"DELETE"})
