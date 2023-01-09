from django.shortcuts import render
from .models import Product, Category,ProductImage




#def index_view(request):
    #prods= Product.objects.order_by("id")
    #image=ProductImage.objects.all()

    #context={
        #"prods": prods,
        #"image":image
    #}
    #print(image,"bunuda gor")
    #return render(request,"index.html",context)
