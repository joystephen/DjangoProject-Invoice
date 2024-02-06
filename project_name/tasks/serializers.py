from rest_framework import serializers
from .models import InvoiceHeader, InvoiceBillSundry, InvoiceItem

class InvoiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceHeader
        fields = '__all__'

class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
