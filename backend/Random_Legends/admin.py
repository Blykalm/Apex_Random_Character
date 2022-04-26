from django.contrib import admin
from .models import Legend

class LegendAdmin(admin.ModelAdmin):
    display = ('name')

# Register your models here.
admin.site.register(Legend, LegendAdmin)
