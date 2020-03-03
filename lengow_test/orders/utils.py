from xml.etree import ElementTree

import requests

from .models import Order


# Fetch original data from xml file
def fetch_original_data():
    res = requests.get('http://test.lengow.io/orders-test.xml')

    tree = ElementTree.fromstring(res.content)
    for child in tree.findall('orders'):
        for subchild in child:
            if Order.objects.all().filter(order_id=subchild.find('order_id').text):
                continue
            order = Order(
                marketplace=subchild.find('marketplace').text,
                id_flux=int(subchild.find('idFlux').text),
                order_id=subchild.find('order_id').text,
                order_mrid=subchild.find('order_mrid').text,
                order_refid=subchild.find('order_refid').text
            )
            order.save()
