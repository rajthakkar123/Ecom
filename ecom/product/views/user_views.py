
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
import random
from django.views.generic import TemplateView, CreateView,ListView, UpdateView
from user.models import CustomUser
from user.forms import AddressForm, NewUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from product.models import Product,Subcategory,Order,OrderItems,Category,Cart,CartItems,Order, OrderItems 
from user.models import Address 
from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import json

# Create your views here.




class ViewAddress(LoginRequiredMixin,ListView):
    template_name = 'user/view-address.html'
    model = Address
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = self.request.user
        address = Address.objects.filter(user = user)
        context["address"] =address
        print(context)
        return context

class UpdateAddress(LoginRequiredMixin,UpdateView):
    template_name = "user/update-address.html"
    model= Address
    success_url= "/view-address/"
    fields = ["Flat_number_society","landmark","area","city","pincode"]
    def get_object(self, queryset=None):
        id = self.kwargs.get('id')  # Retrieve the 'id' parameter from the URL
        obj = Address.objects.get(id=id)
        return obj
    
class AddAddress(LoginRequiredMixin,CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'user/add-address.html'
    success_url= '/'
    # @login_required
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        form = AddressForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
        
        
class LoadHome(TemplateView): 
    template_name = 'user/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = list(Product.objects.all())
        # change 3 to how many random items you want
        random_items = random.sample(items, 3)
        context['product_list'] = random_items
        print("Context: ",context)
        return context


class LoadCategory(TemplateView):
    template_name = 'user/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['category_vo_list'] = Category.objects.all()
        return context



class LoadProduct(TemplateView):
    template_name = 'user/single-product.html'


class LoadCart(LoginRequiredMixin,TemplateView):
    template_name = 'user/cart.html'
    

    def get_context_data (self, **kwargs):
        context = super(LoadCart,self).get_context_data(**kwargs)
        request = self.request
        user = request.user
        user_cart  = Cart.objects.get(user_id = user.id)
        cart_items = CartItems.objects.filter(cart_id = user_cart.id).select_related('item_name')
        cart_items = cart_items.order_by('id')
        for item in cart_items:
            item.image = item.item_name.image.url
            print(item.image)
        total = 0.00
        for i in cart_items:
            i.amount = i.price * i.quantity
            i.amount = float(i.amount)
            total = total + i.amount
        context["cart"] = cart_items
        context["total"] = total
        print(context)

        return context
        
class LoadCheckout(LoginRequiredMixin,TemplateView):
    template_name = 'user/checkout.html'

    def get_context_data (self, **kwargs):
        context = super(LoadCheckout,self).get_context_data(**kwargs)
        
        request = self.request
        user = request.user
        user_cart  = Cart.objects.get(user_id = user.id)
        cart_items = CartItems.objects.filter(cart_id = user_cart.id).select_related('item_name')
        cart_items = cart_items.order_by('id')
        total = 0.00
        for i in cart_items:
            i.amount = i.price * i.quantity
            i.amount = float(i.amount)
            total = total + i.amount
        context["cart"] = cart_items
        context["total"] = total

        return context

class LoadContact(TemplateView):
    template_name = 'user/contact.html'


class LoadBlog(TemplateView):
    template_name = 'user/blog.html'

class LoadConfirmation(LoginRequiredMixin,TemplateView):
    template_name = 'user/confirmation.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        user = self.request.user

        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        latest_order_items = OrderItems.objects.filter(main_order = latest_order)

        for i in latest_order_items:
            i.total = i.quantity*i.price

        context["order"] = latest_order
        context["order_items"] = latest_order_items

        return context

class LoadSingleBlog(TemplateView):
    template_name = 'user/single-blog.html'


class LoadTracking(TemplateView):
    template_name = 'user/tracking.html'


class LoadLogin(LoginView):
    template_name = 'user/login.html'


class LoadElements(TemplateView):
    template_name = 'user/elements.html'
    
def ajax_load_product(request, id):
    category = Category.objects.get(id=id)
    product_vo_list = Product.objects.filter(category_id=category)
    context = {'product_vo_list': product_vo_list}
    products_list = list(product_vo_list.values())
    return JsonResponse({'products': products_list})
    
class LoadRegistration(CreateView):
    model = CustomUser
    form_class= NewUserForm
    template_name = 'user/register.html'
    
    def get_success_url(self):
        return reverse('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        cart = Cart(user=self.object)
        cart.save()
        
        return response

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_filtered = Product.objects.get(id = product.id)
    cart_item, created = CartItems.objects.get_or_create(cart=cart, item_name=product_filtered)
    
    cart_item.price = product_filtered.price
    
    if cart_item.quantity == None:
        cart_item.quantity = 1
        cart_item.save() 
            
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect("home")

def remove_from_cart(request,product_id):
    cart_item = CartItems.objects.get(id = product_id)

    if cart_item.quantity ==1:
        cart_item.delete()  

    else:
        cart_item.quantity-=1
        cart_item.save()

    return redirect('cart')

def add_in_cart(request,product_id):
    cart_item = CartItems.objects.get(id = product_id)
    cart_item.quantity +=1
    cart_item.save()

    return redirect('cart')



def OrderCreation(request,**kwargs):
    user = request.user
    cartt = Cart.objects.get(user = user)
    csrf_token = request.META.get('HTTP_X_CSRFTOKEN')

    cart_data = json.loads(request.body.decode('utf-8'))
    
    order = Order.objects.create(user = user)
    for item in cart_data:
        item_name = item['item_name']
        quantity = item['quantity']
        amount = item['amount']
        
        price = float(amount) / int(quantity)
        order.total += float(amount)
        OrderItems.objects.create(product = item_name,quantity = quantity,price = price,main_order=order)
        
    order.save()
        
    CartItems.objects.filter(cart=cartt).delete()
    response_data = {'message': 'Order created successfully'}
    
    return JsonResponse(response_data)


class UserProfile( SuccessMessageMixin, UpdateView):
    model = CustomUser
    fields = ['email', 'first_name', 'last_name']
    template_name = 'user/profile.html'
    success_url = reverse_lazy('home')
    success_message = 'Your profile has been updated successfully.'

    def get_object(self, queryset=None):
        return self.request.user
