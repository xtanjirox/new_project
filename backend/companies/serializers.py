from rest_framework import serializers
from .models import Company, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name', 'symbol']

class CompanySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)
    currency_id = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all(), source='currency', write_only=True)

    class Meta:
        model = Company
        fields = '__all__'
