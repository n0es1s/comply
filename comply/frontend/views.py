from django.shortcuts import render
from .models import Location, Product, User

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

# Create your views here.
@login_required
def index(request):
    company = request.user.company
    location_limit = company.location_limit
    locations = Location.objects.filter(company=company)
    active_locations = len(Location.objects.filter(company=company))

    user_count = len(User.objects.filter(company=company))
    products_size = 0

    for store in locations:
        store_products_len = len(Product.objects.filter(location=store))
        products_size += store_products_len


    context = {
        'active_locations': active_locations,
        'location_limit': location_limit,
        'products_size': products_size,
        'user_count': user_count,
        'company': company,
    }

    return render(request, 'frontend/dashboard.html', context)



@login_required
def locations(request):
    user = request.user.first_name
    company = request.user.company

    locations = Location.objects.filter(company=company)

    context = {
                'locations': locations,
                'name': user,
                }

    return render(request, 'frontend/locations.html', context)


@login_required
def products(request):
    company = request.user.company
    locations = Location.objects.filter(company=company)
    products = list()

    for store in locations:
        store_products = Product.objects.filter(location=store)
        for each in store_products:
            products.append(each)

    context = {
                'products': products,
                }

    return render(request, 'frontend/products.html', context)



def register(request):

    return render(request, 'frontend/register.html')
