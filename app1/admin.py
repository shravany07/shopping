
from django.contrib import admin

from .models import Pro, Signup, contact_us,fpro

admin.site.register(Signup)
admin.site.register(contact_us)

class proadmin(admin.ModelAdmin):
    list_display=['name','price','des','review']
admin.site.register(Pro,proadmin)

admin.site.register(fpro)