from django.db import models
from django.core.validators import RegexValidator


class Seller(models.Model):
    VAT = "VAT"
    NON_VAT = "NON_VAT"

    VAT_STATUS_CHOICES = [
        (VAT, "VAT Registered"),
        (NON_VAT, "Non-VAT Registered"),
    ]

    registered_business_name = models.CharField(max_length=255)
    business_address = models.TextField()
    tin = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{3}-\d{3}-\d{3}-\d{3}$',
                message="TIN must be in format 000-000-000-000"
            )
        ]
    )
    branch_code = models.CharField(max_length=10, blank=True, null=True)
    vat_status = models.CharField(
        max_length=10,
        choices=VAT_STATUS_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def vat_reg_tin_phrase(self):
        if self.vat_status == self.VAT:
            return f"VAT REG. TIN: {self.tin}"
        return None

    def __str__(self):
        return self.registered_business_name


class BusinessCompliance(models.Model):
    seller = models.OneToOneField(
        Seller,
        on_delete=models.CASCADE,
        related_name="compliance"
    )

    has_registered_books = models.BooleanField(default=False)
    has_registered_pos = models.BooleanField(default=False)
    has_cas_permit = models.BooleanField(default=False)
    cas_permit_number = models.CharField(max_length=100, blank=True, null=True)
    printed_by_accredited_printer = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Compliance - {self.seller.registered_business_name}"