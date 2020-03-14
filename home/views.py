from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from home.models import product
from home.forms import formUser, formCustomer 
from home.models import user, appointment
from home.models import post as p
from django.contrib.auth.hashers import make_password
from cart.forms import CartAddProductForm 
# Create your views here.
def index(request) : 
    product_list = product.objects.all()
    _paginator = Paginator(product_list,6) 
    page = request.GET.get('page')
    products = _paginator.get_page(page)
    form = formUser()
    if request.method == 'POST' : 
        form = formUser(request.POST, user) 
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm'] : 
            request.POST.mutable = True 
            post = form.save(commit = False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.password = make_password(form.cleaned_data['password'])
            # post.password = form.cleaned_data['password']
            post.save() 
        elif form.cleaned_data['password'] != form.cleaned_data['confirm'] : 
            form.add_error('confirm', 'the password does not match')
    # customer 
    return render(request, 'home/index.html', {'sanpham' : products, 'form' : form})
def about(request) : 
    form1 = formCustomer()
    if request.method == 'POST' : 
        form1 = formCustomer(request.POST, appointment)
        if form1.is_valid() : 
            request.POST.mutable = True 
            post = form1.save(commit = False)
            post.name = form1.cleaned_data['name']
            post.email = form1.cleaned_data['email']
            post.service = form1.cleaned_data['service']
            post.barder = form1.cleaned_data['barder']
            post.date = form1.cleaned_data['date']
            post.time = form1.cleaned_data['time']
            post.save() 
    return render(request, 'home/about.html', {'form1' : form1})
# def blog(request) : 
#     return render(request, 'home/blog.html')
# def contact(request) : 
#     return render(request, 'home/contact.html')
# def elements(request) : 
#     return render(request, 'home/elements.html')
# def main(request) : 
#     return render(request, 'home/main.html')
# def service(request) : 
#     return render(request, 'home/service.html')
# def single(request) : 
#     return render(request, 'home/single-blog.html') 

# def list1(request) : 
#     return render(request, 'home/list.html', {'post' : p.objects.all()}) 
# def post_page(request, id) : 
#     post1 = p.objects.get(id=id)
#     return render(request, 'home/post.html', {'post': post1})
def detail(request, id) : 
    form = CartAddProductForm()
    product_detail = product.objects.get(id=id)
    return render(request, 'home/detail.html', {'product' : product_detail, 'cart_product_form' : form})

# def login(request) : 
#     return render(request, 'home/login.html')