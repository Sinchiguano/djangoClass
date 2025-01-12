from django.urls import path
from . import views


urlpatterns = [
    path("product/list",views.product_list,name="product_list"),
    path("product/update/<int:product_id>",views.product_update,name="product_update"),
    path("product/delete",views.product_delete,name="product_delete"),
    path("product/register",views.product_register,name="product_register"),
    path("product/create/<int:day>/<str:month>/<int:year>",views.product_create,name="product_create"),

]