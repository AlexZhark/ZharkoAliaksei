from django.db import models

# Create your models here.
class Catalog(models.Model):
    
    image = models.ImageField(upload_to='uploads')
    title = models.CharField(blank=False, max_length=30)
    content = models.TextField(blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Review(models.Model):

    author = models.CharField(blank=False, max_length=20)
    email = models.EmailField(blank=False)
    comment = models.TextField(blank=False)
    image = models.ImageField(upload_to='reviews', blank=False)
    date = models.TextField(blank=False, default="12:00, 12.12.2023")

    def __str__(self) -> str:
        return self.author
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


    # date = models.DateTimeField()