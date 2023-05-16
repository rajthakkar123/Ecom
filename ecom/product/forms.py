from django.forms import ModelForm
from .models import Category,Subcategory,Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name','category']
        
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','subcategory',"price","image"]

