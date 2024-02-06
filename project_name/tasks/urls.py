from django.urls import path
from .views import (InvoiceListCreateAPIView, InvoiceDetailAPIView, BillSundryDetailAPIView, BillSundryListCreateAPIView,
                    InvoiceItemListCreateAPIView, InvoiceItemDetailAPIView)

urlpatterns = [
    path('invoice-header/', InvoiceListCreateAPIView.as_view(), name='author-list-create'),
    path('invoice-header/<int:pk>/', InvoiceDetailAPIView.as_view(), name='author-retrieve-update'),

    path('bill-sundry/', BillSundryListCreateAPIView.as_view(), name='genre-list-create'),
    path('bill-sundry/<int:pk>/', BillSundryDetailAPIView.as_view(), name='genre-retrieve-update'),

    path('invoice-item/', InvoiceItemListCreateAPIView.as_view(), name='book-list-create'),
    path('invoice-item/<int:pk>/', InvoiceItemDetailAPIView.as_view(), name='genre-retrieve-update'),

]
