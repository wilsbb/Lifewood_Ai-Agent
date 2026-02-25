from django.db import models


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=255)
    buyer_address = models.TextField()
    buyer_tin = models.CharField(max_length=15, blank=True, null=True)
    is_vat_registered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.buyer_name