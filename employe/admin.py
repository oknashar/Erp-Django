from django.contrib import admin
from .models import Employe, Absense
# Register your models here.


class EmployeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telephone', 'salary',)
    list_filter = ('name', 'address', 'telephone', 'salary',)
    search_fields = ('name', 'address', 'telephone', 'salary',)


class AbsenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date','timeIn','timeOut',)
    list_filter = ('name', 'date','timeIn','timeOut',)
    search_fields = ('name', 'date','timeIn','timeOut',)


admin.site.register(Employe, EmployeAdmin)
admin.site.register(Absense,AbsenseAdmin)
