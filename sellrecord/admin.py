from django.contrib import admin
from .models import Sellrecord

admin.site.site_header = 'waaneiza Sellrecord Management System'

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','Price','showroom','paid','date']
    list_filter = ['customer_name','customer_phone','Price','showroom','paid','date']
    search_fields = ['customer_name','customer_phone','Price','showroom','paid','date']

admin.site.register(Sellrecord, SellrecordAdmin)

