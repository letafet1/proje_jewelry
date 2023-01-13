from rest_framework import  serializers

from ..models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=["title","slug","id"]

class ProdsCatSerializer(serializers.ModelSerializer):

    category=CategorySerializer()
    class Meta:
        model=Product
        fields=["id","name","price","category","description","created_date","material","discount_price","discount_price","image_1","image_2"]


#class ProductImageSerializer(serializers.ModelSerializer):
    #product = ProdsCatSerializer()
    #class Meta:
        #model=ProductImage
        #fields=["id","image"]


class ProdsSerializer(serializers.ModelSerializer):

    #def to_representation(self, instance):
        #response = super().to_representation(instance)
        #response['category'] = CategorySerializer(instance.category).data
        #return response

    class Meta:
        model=Product
        fields=["id","name","price","category","description","created_date","material","discount_price","image_1","image_2"]

