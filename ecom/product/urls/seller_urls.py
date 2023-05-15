from django.urls import path
from product.views.seller_views import LoadHome,CreateCategory,CreateSubcategory,CreateProduct,load_ajax_subcategory


urlpatterns = [
    path("admin/",LoadHome.as_view(),name="homepage"),
    path("admin/createcategory/",CreateCategory.as_view(),name="createproduct"),
    path("admin/createsubcategory/",CreateSubcategory.as_view(),name= 'createsubcategory'),
    path('admin/createproduct/',CreateProduct.as_view(),name="createproduct"),
    path("admin/load-product-subcategory",load_ajax_subcategory,name="ajax_load_subcategory" ),
]