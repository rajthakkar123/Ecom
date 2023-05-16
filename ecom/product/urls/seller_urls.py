from django.urls import path
from product.views.seller_views import load_ajax_subcategory
from product.views import seller_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/",seller_views.LoadHome.as_view(),name="homepage"),
    path("admin/logout/",LogoutView.as_view(),name="logout"),
    path("admin/createcategory/",seller_views.CreateCategory.as_view(),name="createcategory"),
    path("admin/createsubcategory/",seller_views.CreateSubcategory.as_view(),name= 'createsubcategory'),
    path('admin/createproduct/',seller_views.CreateProduct.as_view(),name="createproduct"),
    path("admin/load-product-subcategory",load_ajax_subcategory,name="ajax_load_subcategory" ),
    path("admin/updatecategory/<int:pk>",seller_views.UpdateCategory.as_view(),name="updatecategory"),
    path("admin/updatesubcategory/<int:pk>",seller_views.UpdateSubcategory.as_view(),name="updatesubcategory"),
    path("admin/updateproduct/<int:pk>",seller_views.UpdateProduct.as_view(),name="updateproduct"),
    path("admin/deletecategory/<int:pk>",seller_views.DeleteCategory.as_view(),name="deletecategory"),
    path("admin/deletesubcategory/<int:pk>",seller_views.DeleteSubcategory.as_view(),name="deletesubcategory"),
    path("admin/deleteproduct/<int:pk>",seller_views.DeleteProduct.as_view(),name="deleteproduct"),
]