from django.urls import path
from product.views.seller_views import load_ajax_subcategory
from product.views import seller_views

urlpatterns = [
    path("admin/",seller_views.LoadHome.as_view(),name="homepage"),
    path("admin/createcategory/",seller_views.CreateCategory.as_view(),name="createcategory"),
    path("admin/createsubcategory/",seller_views.CreateSubcategory.as_view(),name= 'createsubcategory'),
    path('admin/createproduct/',seller_views.CreateProduct.as_view(),name="createproduct"),
    path("admin/load-product-subcategory",load_ajax_subcategory,name="ajax_load_subcategory" ),
    path("admin/updatecategory/<int:pk>",seller_views.UpdateCategory.as_view(),name="updatecategory"),
    path("admin/updatesubcategory/<int:pk>",seller_views.UpdateSubcategory.as_view(),name="updatesubcategory"),
    path("admin/updateproduct/<int:pk>",seller_views.UpdateProduct.as_view(),name="updateproduct"),
]