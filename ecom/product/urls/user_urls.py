from django.urls import path
from product.views.user_views import SearchResultsView,ListOrder,OrderCreation,UserProfile,ViewAddress,UpdateAddress, add_in_cart,remove_from_cart,add_to_cart,ajax_load_product ,LoadRegistration,LoadHome,LoadCategory,LoadCart,LoadCheckout,LoadConfirmation,LoadLogin,AddAddress
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path("",LoadHome.as_view(),name="home"),
    path("category/",LoadCategory.as_view(),name="category"),
    path("cart/",LoadCart.as_view(),name="cart"),
    path("checkout/",LoadCheckout.as_view(),name="checkout"),
    path("confirmation/",LoadConfirmation.as_view(),name="confirmation"),
    path("login/",LoadLogin.as_view(),name="login"),
    path("registration/",LoadRegistration.as_view(),name="registration"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path('add-address/',AddAddress.as_view(),name="add-address"),
    path('view-address/',ViewAddress.as_view(),name="view-address"),
    path('update-address/<int:id>',UpdateAddress.as_view(),name="update-address"),
    path("category/load-categories/<int:id>/",ajax_load_product, name="ajax_load_product" ),
    path('add-to-cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path("remove-from-cart/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("add-in-cart/<int:product_id>/", add_in_cart, name="add_in_cart"),
    path("confirm-order/",OrderCreation,name="confirm-order"),
    path('profile/update/', UserProfile.as_view(), name='user-update'),
    path('past-orders',ListOrder.as_view(),name="past-orders"),
    path('search_results/',SearchResultsView.as_view(),name="search_results"),
    
]
