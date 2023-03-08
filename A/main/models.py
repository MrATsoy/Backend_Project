from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    article_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/', default='default_photo.jpg')
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 60})
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    general_information = models.TextField()

    def __str__(self):
        return self.name