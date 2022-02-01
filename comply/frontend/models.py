from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('EXTERNAL', 'External'),
    )
    phone_number = PhoneNumberField(blank=True)
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=True, blank=True, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)


class Company(models.Model):
    COMPANY_TYPE_CHOICES = [
        ('DISPENSARY','Dispensary'),
        ('PROCESSOR','Processor'),
        ('GROWER','Grower'),
        ('TRANSPORT', 'Transport'),
        ('LAB', 'Lab'),
        ('OTHER','Other'),

    ]
    company_name = models.CharField(max_length=254, blank=False)
    company_type = models.CharField(max_length=25, choices=COMPANY_TYPE_CHOICES, default='OTHER')
    company_dba = models.CharField(max_length=254, blank=False)
    location_limit = models.PositiveIntegerField(null=True, blank=False)
    address = models.TextField()


    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name

class Location(models.Model):
    LOCATION_TYPE_CHOICES = [
        ('DISPENSARY','Dispensary'),
        ('PROCESSOR','Processor'),
        ('GROWER','Grower'),
        ('TRANSPORT', 'Transport'),
        ('LAB', 'Lab'),
        ('OTHER','Other'),

    ]
    location_name = models.CharField(max_length=254, blank=True)
    location_type = models.CharField(max_length=100, choices=LOCATION_TYPE_CHOICES, blank=False)
    location_dba = models.CharField(max_length=254, blank=False)
    license_number = models.CharField(max_length=12, unique=True)
    company = models.ForeignKey(Company, null=True, blank=True,on_delete=models.SET_NULL,)
    active = models.BooleanField(default=False)


    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        license = str(self.license_number).upper()
        license = '{}-{}-{}'.format(license[:4], license[4:8], license[8:])

        return f"{self.location_name}({license})"


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('FLOWER','Flower'),
        ('CONCENTRATE','Concentrate'),
        ('EDIBLE','Edible'),
        ('TINCTURE','Tincture'),
        ('TOPICAL','Topical'),
        ('OTHER','Other'),
    ]
    product_name = models.CharField(max_length=254, blank=True)
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPE_CHOICES, blank=False)
    product_description = models.TextField(blank=True)
    batch_id = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )
    notes = models.TextField(blank=True)

    location = models.ForeignKey(Location, null=True, blank=True,on_delete=models.SET_NULL,)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,

    )
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name


class ProductFileType(models.Model):
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Product File Type'
        verbose_name_plural = 'Product File Types'

    def __str__(self):
        return self.name


class ProductFile(models.Model):
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL,)
    file_type = models.ForeignKey(ProductFileType,null=True,on_delete=models.SET_NULL,)
    file = models.FileField(
        blank=True,
    )
    notes = models.TextField(blank=True)
