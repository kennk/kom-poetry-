from django.contrib import admin
from .models import Itanikom

class ItanikomAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Itanikom, ItanikomAdmin)
# Register your models here.
