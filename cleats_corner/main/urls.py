from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_of_products, name="list_of_products"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
]