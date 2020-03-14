from django.shortcuts import render, redirect, get_list_or_404, HttpResponse
from django.views.decorators.http import require_POST
from home.models import product as product1
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.hashers import make_password


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_list_or_404(product1, id=product_id)
    if 'price' not in request.POST:
        price = 0
    else:
        price = request.POST['price']
    form = CartAddProductForm()
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, price=product.price, quantity=int(
            cd['quantity'], update_quantity=cd['update_quantity']))
    return redirect('cart:cart_detail')


def cart_remove(self, product_id):
    cart = Cart(request)
    product = get_list_or_404(product1, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# class loginclass(View):
#     def get(self, request):
#         return render(request, 'home/login.html')

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return HttpResponse("User not found")
#         login(request, user)
#         # return render(request, 'home/index.html')
#         # return HttpResponse("login successfully")
#         return redirect('cart:cart_detail')


class cart_detail(LoginRequiredMixin, View):
    login_url = '/cart/loginclass/'

    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'], 'update': True})
            print(item['update_quantity_form'])
        return render(request, 'cart/detail.html', {'cart': cart})
