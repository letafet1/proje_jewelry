from  django.urls import path
from django.conf.urls import url
from . import views

app_name="product-api"

urlpatterns=[
    path("list/", views.prods_list_view, name="list"),
    path("otherlist/", views.ProdsListView.as_view(), name="otherlist"),
    path("theotherlist/", views.ProdsTheListView.as_view(), name="theotherlist"),
    path("thecategorylist/", views.CategoryTheListView.as_view(), name="thecategorylist"),
    path("thecategoryproductlist/", views.CategoryProductView.as_view(), name="thecategoryproductlist"),
    ]