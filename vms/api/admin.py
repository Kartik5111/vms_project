from django.contrib import admin
from .models import Vendor,PurchaseOrder,HistoricalPerformance
# Register your models here.
class vendorAdmin(admin.ModelAdmin):
    list_display=('name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
admin.site.register(Vendor,vendorAdmin)


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


from .models import HistoricalPerformance

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('vendor', 'date')
    search_fields = ('vendor__name',)  # Assuming 'name' is a field in the Vendor model

admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)