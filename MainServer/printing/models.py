from django.db import models
from datetime import timedelta


class PrinterAccreditation(models.Model):
    authority_to_print_number = models.CharField(max_length=100)
    atp_issue_date = models.DateField()
    bir_permit_number = models.CharField(max_length=100)

    printer_name = models.CharField(max_length=255)
    printer_address = models.TextField()
    printer_tin = models.CharField(max_length=15)

    serial_start = models.CharField(max_length=50)
    serial_end = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def valid_until_date(self):
        return self.atp_issue_date.replace(
            year=self.atp_issue_date.year + 5
        )

    def __str__(self):
        return f"ATP {self.authority_to_print_number}"