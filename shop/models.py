from django.db import models
from jsonfield import JSONField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db.models import PointField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    parentId = models.ForeignKey("self", related_name='sub_categories', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'parentId',)
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
    label = models.CharField(max_length=15, db_index=True)

    class Meta:
        ordering = ('label',)

    def __str__(self):
        return self.label


class UnitConversion(models.Model):
    from_unit = models.ForeignKey(Unit, related_name='from_units', on_delete=models.CASCADE)
    to_unit = models.ForeignKey(Unit, related_name='to_units', on_delete=models.CASCADE)
    number_of_multiples = models.ForeignKey(Unit, related_name='numbers', on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    address = models.CharField(max_length=100, db_index=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    location = PointField(null=True, blank=True)
    active_inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Sale(models.Model):
    bill_number = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, related_name='sales', on_delete=models.SET)
    receive_amount = models.IntegerField(default=0, null=True, blank=True)
    return_amount = models.IntegerField(default=0, null=True, blank=True)
    due_amount = models.IntegerField(default=0, null=True, blank=True)
    total_amount = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ('bill_number',)


class Row(models.Model):
    sale = models.ForeignKey(Sale, related_name='rows', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='rows', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    unit = models.ForeignKey(Unit, related_name='rows', on_delete=models.SET)
    discount = models.DecimalField(max_digits=6, decimal_places=2)