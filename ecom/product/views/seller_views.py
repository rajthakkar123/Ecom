from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from product.models import Category,Subcategory,Product
from product.forms import CategoryForm,SubCategoryForm,ProductForm
from django.forms import model_to_dict
import json 
from django.urls import reverse

# Create your views here.
from ecom.mixins import SuperUserRequiredMixin


class LoadHome(SuperUserRequiredMixin, TemplateView):
    template_name = 'seller/index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LoadHome,self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["subcategories"] = Subcategory.objects.all()
        context["products"] = Product.objects.all()
        return context

class CreateCategory(SuperUserRequiredMixin ,CreateView):
    model = Category
    form_class = CategoryForm
    template_name= "seller/createcategory.html"
    success_url = "/admin/createcategory"


class CreateSubcategory(SuperUserRequiredMixin ,CreateView):
    model=Subcategory
    form_class = SubCategoryForm
    template_name = 'seller/createsubcategory.html'
    success_url = '/admin/createsubcategory'
    def get_context_data(self,*args, **kwargs):
        context = super(CreateSubcategory, self).get_context_data(*args,**kwargs)
        context['categorylist'] = Category.objects.all()
        return context


class CreateProduct(SuperUserRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = "/admin/createproduct"
    template_name = 'seller/createproduct.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super(CreateProduct, self).get_context_data(*args,**kwargs)
        context['categorylist'] = Category.objects.all()
        return context
        

def load_ajax_subcategory(request):
    category_id = request.GET.get('categoryID')
    category = Category.objects.get(id = category_id)
    
    subcategory_vo_list = Subcategory.objects.filter(category_id = category.id)
    
    json_subcategory_list = []
    
    for i in subcategory_vo_list:
        dict = model_to_dict(i)
        json_subcategory_list.append(dict)
    return HttpResponse (json.dumps(json_subcategory_list), content_type = "application/json")
    
class UpdateCategory(UpdateView):
    model =Category
    template_name = "seller/update-category.html"
    form_class = CategoryForm
    success_url = "/admin/"
    
class UpdateSubcategory(UpdateView):
    model =Subcategory
    template_name = "seller/update-subcategory.html"
    form_class = SubCategoryForm
    success_url = "/admin/"

class UpdateProduct(UpdateView):
    model =Product
    template_name = "seller/update-product.html"
    form_class = ProductForm
    success_url = "/admin/"
    
class DeleteCategory(DeleteView):
    model = Category
    success_url = "/admin"
    template_name = "seller/confirm_delete.html"

class DeleteSubcategory(DeleteView):
    model = Subcategory
    success_url = "/admin"
    template_name = "seller/confirm_delete.html"

class DeleteProduct(DeleteView):
    model = Product
    success_url = "/admin"
    template_name = "seller/confirm_delete.html"