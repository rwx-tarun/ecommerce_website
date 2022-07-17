from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):
    def get(self,request):
        queryset = Product.objects.all()
        serializers = ProductSerializers(queryset,many=True)
        return Response(serializers.data)
    
    def delete(self,request):
        data = request.data
        product = Product.objects.get(id = data.get("id"))
        product.delete()

        queryset = Product.objects.all()
        serializers = ProductSerializers(queryset,many=True)
        return Response(serializers.data)

