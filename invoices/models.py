from django.db import models


class Invoice(models.Model):
	number = models.CharField(max_length=50, unique=True)
	customer = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField(blank=True)

	def __str__(self) -> str:
		return f"Invoice {self.number} - {self.customer} (${self.amount})"
