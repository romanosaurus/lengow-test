from django.db import models
from django.forms import ModelForm

# Create your models here.


class Order(models.Model):
    marketplace = models.CharField(max_length=30)
    id_flux = models.IntegerField()
    order_id = models.CharField(max_length=30)
    order_mrid = models.CharField(max_length=30)
    order_refid = models.CharField(max_length=30)

    def __str__(self):
        return self.order_id


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['marketplace', 'id_flux', 'order_id', 'order_mrid', 'order_refid']
