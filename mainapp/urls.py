
from django.urls import path
from mainapp import views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name ='products'),
    path('catgory/<int:pk>/', mainapp.ProductsListView.as_view(), name ='category'),
    # path('catgory/<int:pk>/<page>/', mainapp.products, name ='category_page'),
    path('product/<int:pk>/', mainapp.product, name ='product'),
]
