from django.db import models
from jsonfield import JSONField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    brand = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)
    extra = JSONField(null=True, blank=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
