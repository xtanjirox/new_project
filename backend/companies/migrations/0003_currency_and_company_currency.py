from django.db import migrations, models


def create_currencies(apps, schema_editor):
    Currency = apps.get_model('companies', 'Currency')
    currencies = [
        {'code': 'EUR', 'name': 'Euro', 'symbol': '€'},
        {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
        {'code': 'GBP', 'name': 'British Pound', 'symbol': '£'},
        {'code': 'JPY', 'name': 'Japanese Yen', 'symbol': '¥'},
        {'code': 'CHF', 'name': 'Swiss Franc', 'symbol': 'Fr'},
        {'code': 'CAD', 'name': 'Canadian Dollar', 'symbol': '$'},
        {'code': 'AUD', 'name': 'Australian Dollar', 'symbol': '$'},
        {'code': 'CNY', 'name': 'Chinese Yuan', 'symbol': '¥'},
        {'code': 'INR', 'name': 'Indian Rupee', 'symbol': '₹'},
        {'code': 'BRL', 'name': 'Brazilian Real', 'symbol': 'R$'},
    ]
    for c in currencies:
        Currency.objects.get_or_create(code=c['code'], defaults={'name': c['name'], 'symbol': c['symbol']})


def set_default_currency(apps, schema_editor):
    Company = apps.get_model('companies', 'Company')
    Currency = apps.get_model('companies', 'Currency')
    try:
        euro = Currency.objects.get(code='EUR')
        Company.objects.filter(currency_id__isnull=True).update(currency=euro)
    except Currency.DoesNotExist:
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_tva_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('symbol', models.CharField(max_length=8, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='company',
            name='currency',
            field=models.ForeignKey(to='companies.Currency', on_delete=models.SET_DEFAULT, default=1, related_name='companies'),
        ),
        migrations.RunPython(create_currencies, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(set_default_currency, reverse_code=migrations.RunPython.noop),
    ]
