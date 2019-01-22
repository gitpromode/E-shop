from django.db import models
from jsonfield import JSONField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db.models import PointField

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


class Unit(models.Model):
    label= models.CharField(max_length=15, db_index=True)

    class Meta:
        ordering = ('label')

    def __str__(self):
        return self.label


class UnitConversion(models.Model):
    from_unit = models.ForeignKey(Unit, related_name='from', on_delete=models.CASCADE)
    to_unit = models.ForeignKey(Unit, related_name='to', on_delete=models.CASCADE)
    number_of_multiples = models.ForeignKey(Unit, related_name='numbers', on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    address = models.CharField(max_length=100, db_index=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    location = PointField(null=True, blank=True)

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name