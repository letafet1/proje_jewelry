from django.db import models
from  django.contrib.auth import get_user_model
from product.helper import seo
from django.urls import reverse

User=get_user_model()

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="category_name",null=True)
    slug = models.SlugField(verbose_name="Slug", editable=False, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:category_detail', kwargs={'slug': self.slug})

class Product (models.Model):

    name=models.CharField(max_length=200,verbose_name="prods_name",null=True )
    description = models.TextField(null=True)
    price=models.FloatField(null=True)
    discount_price = models.FloatField(default=0)
    material=models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="post_category", related_query_name="pcategory")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    image_1 = models.ImageField(upload_to="product_images",null=True)
    image_2 = models.ImageField(upload_to="product_images",null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
        ordering=["-id"]



