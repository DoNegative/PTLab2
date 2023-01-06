from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, Promo


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['person', 'address', 'product', 'price']

    def form_valid(self, form):
        self.object = form.save()
        promo = None
        if self.request.POST['promo']:
            promo = self.request.POST['promo']
        price = Product.objects.get(pk=self.request.POST['product']).price
        if promo:
            discount = Promo.objects.get(name=promo).discount
            price = price * (100 - discount)/100
        self.object.price = price
        self.object.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}, ваша цена со скидкой {self.object.price}!')

