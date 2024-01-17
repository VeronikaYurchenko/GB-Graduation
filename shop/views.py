from django.shortcuts import render, HttpResponseRedirect
from shop.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title': 'OnlineShop'
    }
    return render(request, 'shop/index.html', context)


def products(request, category_id=None):
    context = { 'title': 'OnlineShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'shop/products.html', context)

@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
