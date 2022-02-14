
from attr import field
from django import forms
from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.forms import ModelForm


class ShopUserAdminEditForn(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('is_active',)
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.help_text = ''
        self.fields['password'].attrs['class'] = 'asdasdasd'


class ProductCategoryEditForm(ModelForm):
    discount = forms.IntegerField(label='скидка', min_value=0, max_value=90, initial=0, required=False)

    class Meta:
        model = ProductCategory
        # fields = '__all__'
        exclude = ('is_active',)
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
        # self.fields['password'].attrs['class'] = 'asdasdasd'



