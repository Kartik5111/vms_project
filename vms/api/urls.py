from django.contrib import admin
from django.urls import path,include
from .views import PurchaseOrderViewset,VendorViewset,HistoricalPerformanceViewset
from rest_framework import routers


router =routers.DefaultRouter()
router.register(r'purchase',PurchaseOrderViewset)
router.register(r'vendor',VendorViewset)
router.register(r'historical',HistoricalPerformanceViewset)
urlpatterns = [
    path('',include(router.urls)),
  # Include the URLs from your app
]