import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=40, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_adress = models.CharField(max_length=80, null=False, blank=False)
    delivery_adress = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=18)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number_(self):
        """
        generate random, unique order number using uuid
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        update grand_total each time a new line is added
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < 150:
            self.delivery_cost = 18
        else:
            self.delivery_cost = 0
        self.grand_total = self.delivery_cost + self.order_total
        self.save()

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name="lineitems")
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False,blank=False,default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self,*args, **kwargs):
        """
        override original save method to set new lineitem total and update order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        
        def __str__(self):
            return f'SKU {self.product.sku} on order {self.order.order_number}'
            

