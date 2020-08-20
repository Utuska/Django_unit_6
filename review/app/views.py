from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)

load = []
def product_view(request, pk):
    template = 'app/product_detail.html'
    review = Review.objects.all().filter(product__id=pk)
    product = get_object_or_404(Product, id=pk)


    load.append(pk)
    print(load)
    #request.session['reviewed_products'] = []
    #request.session['reviewed_products'].append(pk)
    #print(request.session['reviewed_products'])

    if load.count(pk) > 1:
        is_review_exist = True
    else:
        is_review_exist = False


    form = ReviewForm(initial={"product": product})

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'product': product,
        'reviews': review,
        'exist': is_review_exist
    }

    return render(request, template, context)
