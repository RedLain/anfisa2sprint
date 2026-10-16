from django.shortcuts import render
from ice_cream.models import IceCream, Category
from django.db.models import Q


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        Q(is_published=True) & (Q(is_on_main=True) | Q(title__icontains='пломбир'))
    )
    # categories = Category.objects.values(
    #     'id', 'output_order', 'title'
    # ).order_by(
    #     'id', 'output_order', 'title'
    # )
    context = {
        'ice_cream_list': ice_cream_list
        # 'categories': categories
        }
    return render(request, template_name, context)
