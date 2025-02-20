# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('<int:product_id>/', views.product_detail, name='product_detail'),
#     path('<int:product_id>/restock/', views.restock_product, name='restock_product'),
# ]
from  django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),  # Homepage
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/restock/', views.restock_product, name='restock_product'),
    # path('', include('inventory_management.urls')),
]
