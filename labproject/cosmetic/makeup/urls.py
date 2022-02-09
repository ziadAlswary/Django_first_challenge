from re import I
from django.urls import path

from . import views

urlpatterns = [
    path('makeup/', views.index, name = 'all-makeups'), #domain/makeup/
    path('makeup/Products', views.Products, name = 'all-products'), 
    path('makeup/Brands', views.Brands, name = 'all-brands'), 
    path('makeup/prouducts/<slug:makeup_name>', views.product_details, name = 'makeup-details'),
    path('makeup/brands/<slug:brand_name>', views.brand_details, name = 'brand-details')

]