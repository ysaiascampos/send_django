from django.contrib import admin
from rest.models import Prods
# Register your models here.

@admin.register(Prods)
class ProdsAdmin(admin.ModelAdmin):
    list_display = ['id','ref','zipcode','store','amount']