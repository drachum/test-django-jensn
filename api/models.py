from django.db import models


class Company(models.Model):
    name = models.CharField('Name', max_length=300)
    headquarter = models.OneToOneField(
        "api.Office",
        null=True,
        related_name="headquarter_of",
        on_delete=models.SET_NULL
    )



class Office(models.Model):
    company = models.ForeignKey(
        "api.Company", related_name="offices", on_delete=models.PROTECT
    )
    street = models.CharField(
        'Street', max_length=256, blank=True
    )
    postal_code = models.CharField(
        'Postal Code', max_length=32, blank=True
    )
    city = models.CharField(
        'City', max_length=128, blank=True, null=True
    )
    monthly_rent = models.DecimalField(
        decimal_places=2, max_digits=10, null=False, default=0
    )
