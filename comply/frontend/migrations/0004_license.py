# Generated by Django 3.2.3 on 2022-01-31 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20220131_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(choices=[('DISPENSARY', 'Dispensary'), ('PROCESSOR', 'Processor'), ('GROWER', 'Grower'), ('TRANSPORT', 'Transport'), ('LAB', 'Lab'), ('OTHER', 'Other')], max_length=100)),
                ('license_number', models.CharField(max_length=12, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.company')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
