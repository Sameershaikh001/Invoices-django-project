from django.contrib import admin
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	list_display = ("number", "customer", "date", "amount")
	search_fields = ("number", "customer")
