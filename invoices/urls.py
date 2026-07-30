from django.urls import path
from . import views

app_name = "invoices"

urlpatterns = [
    path("", views.list_invoices, name="list"),
    path("add/", views.add_invoice, name="add"),
    path("<int:pk>/", views.show_invoice, name="show"),
]
