from django.db import models
from django.utils import timezone

from django.core.validators import URLValidator

class OptionalSchemeURLValidator(URLValidator):
    def __call__(self, value):
        if '://' not in value:
            # Validate as if it were http://
            value = 'http://' + value
        super(OptionalSchemeURLValidator, self).__call__(value)

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    tva_rate = models.DecimalField(max_digits=5, decimal_places=2, default=20, help_text="TVA rate (%) applied to all products for this company")
    currency = models.ForeignKey('Currency', on_delete=models.SET_DEFAULT, default=1, related_name='companies')
    
    class Meta:
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.name
