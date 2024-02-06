from django.contrib import admin
from .models import InvoiceHeader, InvoiceBillSundry, InvoiceItem

# Register your models here.
admin.site.register(InvoiceHeader)
admin.site.register(InvoiceBillSundry)
admin.site.register(InvoiceItem)
