from django.contrib import admin
from gymproduct.models import EnquiryModels

# Register your models here.

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("Sr_no","Gender","Name","Age","Phone","email_address","City","our_packages")

admin.site.register(EnquiryModels,EnquiryAdmin)