from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .models import Invoice
import json


def invoice_to_dict(inv: Invoice) -> dict:
	return {
		"id": inv.id,
		"number": inv.number,
		"customer": inv.customer,
		"date": inv.date.isoformat(),
		"amount": str(inv.amount),
		"description": inv.description,
	}


@require_http_methods(["GET"])
def list_invoices(request):
	invoices = Invoice.objects.all().order_by("-date")
	data = [invoice_to_dict(i) for i in invoices]
	return JsonResponse({"invoices": data})


@require_http_methods(["GET"])
def show_invoice(request, pk: int):
	inv = get_object_or_404(Invoice, pk=pk)
	return JsonResponse(invoice_to_dict(inv))


@require_http_methods(["POST"])
def add_invoice(request):
	try:
		payload = json.loads(request.body.decode() or "{}")
	except json.JSONDecodeError:
		return HttpResponseBadRequest("Invalid JSON")

	required = ["number", "customer", "amount"]
	if not all(k in payload for k in required):
		return HttpResponseBadRequest("Missing required fields: number, customer, amount")

	inv = Invoice.objects.create(
		number=payload.get("number"),
		customer=payload.get("customer"),
		amount=payload.get("amount"),
		description=payload.get("description", ""),
	)
	return JsonResponse(invoice_to_dict(inv), status=201)
