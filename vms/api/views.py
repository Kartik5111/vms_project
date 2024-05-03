from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Vendorserializer,PurchaseOrderserializer,HistoricalPerformanceserializer
from .models import Vendor,PurchaseOrder,HistoricalPerformance
# Create your views here.

class VendorViewset(viewsets.ModelViewSet):
    queryset=Vendor.objects.all()
    serializer_class=Vendorserializer


class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderserializer


class HistoricalPerformanceViewset(viewsets.ModelViewSet):
    queryset=HistoricalPerformance.objects.all()
    serializer_class=HistoricalPerformanceserializer