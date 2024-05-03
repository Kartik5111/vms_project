from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance



class Vendorserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Vendor
        fields="__all__"


class PurchaseOrderserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields="__all__"


class HistoricalPerformanceserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=HistoricalPerformance
        fields="__all__"