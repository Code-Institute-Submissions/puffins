from django.shortcuts import render
from products.models import Product
from django.db.models.functions import Lower


def get_highlights(request):
    products = Product.objects.filter(is_featured=True)
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'featured': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'highlights/highlights.html', context)