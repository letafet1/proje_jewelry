import django_filters.rest_framework
from rest_framework.decorators import  api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from product.models import *
from .filter import ProductFilter
from rest_framework.views import  APIView
from django_filters.rest_framework import DjangoFilterBackend


class CategoryProductView(APIView):
    def get(self, request):
        category_obj=Category.objects.all()
        category_serializer=CategorySerializer(category_obj,many=True).data
        data=[]
        for cata in category_serializer:
            prod_obj=Product.objects.filter(category=cata['id'])
            cata['products']=ProdsSerializer(prod_obj,many=True).data
            data.append(cata)

        return Response(data)



class ProductListView(generics.ListAPIView):
    serializer_class = ProdsCatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = Product.objects.all()
        category=request.GET.get("category")
        search=request.GET.get("search")

        return queryset

class CategoryTheListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        request=self.request
        queryset=Product.objects.all()
        category=request.GET.get("category",None)
        if category:
            queryset=request.filter(product__category__id=int(category))
        return queryset

class ProdsTheListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdsCatSerializer


class ProdsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdsSerializer


@api_view(['GET'])
def prods_list_view(request):

    if request.method == 'GET':
        prods = Product.objects.all()
        serializer = ProdsSerializer(prods, many=True)
        return Response(serializer.data)


