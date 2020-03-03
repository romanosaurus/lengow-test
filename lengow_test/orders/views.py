from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Order, OrderForm
from .filters import OrderFilter
from .utils import fetch_original_data

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
            return HttpResponseRedirect('/')
    return render(request, 'add_order.html', {'form': OrderForm})


def detail(request, model_id):
    order = Order.objects.get(id=model_id)

    return render(request, 'detail.html', {'order': order})


def home(request):
    fetch_original_data()
    orders = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=orders)
    return render(request, 'home.html', {'filter': order_filter})
