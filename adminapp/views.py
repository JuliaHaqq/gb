from django import template
from django.contrib.auth.decorators import user_passes_test
from django.db.models import fields
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from adminapp.forms import ProductEditForm, ShopUserAdminEditForn
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.urls import reverse
from django.views.generic import ListView
from mainapp.models import Product, ProductCategory
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserRegisterForm()


    context = {
        'form': user_form        
    }
    return render(request, 'adminapp/user_form.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     context = {
#         'object_list': ShopUser.objects.all().order_by('-is_active')
#     }
#     return render(request, 'adminapp/users.html', context)


class AccessssMixin():

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class UserListView(AccessssMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    



@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForn(request.POST, request.FILES, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserAdminEditForn(instance=current_user)


    context = {
        'form': user_form        
    }
    return render(request, 'adminapp/user_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if current_user.is_active:
            current_user.is_active = False
        else:
            current_user.is_active = True
        current_user.save()
        return HttpResponseRedirect(reverse('adminapp:user_list'))


    context = {
        'object': current_user
    }
    return render(request, 'user_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    context = {
        
    }
    return render(request, '', context)

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_update(request):

    context = {
        
    }
    return render(request, '', context)

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request):
    context = {
        
    }
    return render(request, '', context)

# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request):
#     context = {
        
#     }
#     return render(request, '', context)


class ProductCreateView(AccessssMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        return reverse('adminapp:product_list', args=[self.kwargs['pk']])


# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     context = {
#         'category': get_object_or_404(ProductCategory, pk=pk),
#         'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
#     }
#     return render(request, 'adminapp/products.html', context)


class ProductsListView(AccessssMixin, ListView):
    model = Product
    template_namr = 'adminapp/products.html'

    def get_context_data(self, *args,**kwargs):
        context_data = super().get_context_data( *args ,**kwargs)
        context_data['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        return context_data

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request):
#     context = {
        
#     }
#     return render(request, '', context)

class ProductUpdateView(AccessssMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request):
#     context = {
        
#     }
#     return render(request, '', context)

class ProductDeleteView(AccessssMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])

    # def delete(self, request, *args, **kwargs):
    #     if self.object.is_active:
    #         self.object.is_active = False
    #     else:
    #         self.object.is_active = True
    #     self.object.save()
    #     return HttpResponseRedirect(reverse())



# @user_passes_test(lambda u: u.is_superuser)
# def product_detail(request, pk):
#     context = {
        
#     }
#     return render(request, '', context)


class ProductDetailView(AccessssMixin,DetailView):
    model = Product
    template_name = 'adminapp/product_detail.htm'



