from django import forms
from .models import Category,Color,Type,creator
from product.models import Product
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields= '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= '__all__'

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields= '__all__'

class creatorForm(forms.ModelForm):
    class Meta:
        model = creator
        fields= '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= '__all__'
        exclude = ('barcode',)


