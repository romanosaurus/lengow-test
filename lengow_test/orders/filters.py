from .models import Order
import django_filters


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['marketplace', 'id_flux', 'order_id', 'order_mrid', 'order_refid']
