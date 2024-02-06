from django.db import models

class InvoiceHeader(models.Model): #book
    billingAddress = models.TextField(max_length=200,null=True)
    customerName = models.TextField()
    invoiceNumber = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.invoiceNumber

class InvoiceBillSundry(models.Model): #author
    billSundryName = models.CharField(max_length=100)
    amount = models.TextField()
    invoice = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.billSundryName

class InvoiceItem(models.Model): #Genre
    name = models.CharField(max_length=100)
    itemName = models.TextField()
    quantity= models.TextField()
    price = models.TextField()
    amount = models.TextField()
    invoice = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# Invoice Header -  main
# Id: UUID
# Date: string (UTC)
# InvoiceNumber: number
# CustomerName: string
# BillingAddress
# Foreign key to invoice header
#
# Invoice BillSundry
# Id: UUID
# billSundryName: string
# Amount: decimals: string
# ShippingAddress: string
# GSTIN: string
# TotalAmount: Decimal
#
# Invoice Items
# Id: UUID
# itemName: string
# Quantity: decimal
# Price: decimal
# Amount: decimal
# Foreign key to invoice header


