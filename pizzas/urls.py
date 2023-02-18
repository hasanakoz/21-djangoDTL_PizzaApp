from django.urls import path
from .views import home,pizzas, order_view, my_orders, update_orders_view, delete_order_view

urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
    path('pizzas/<int:id>', order_view, name='order'),
    path('my_orders/', my_orders, name='my_orders'),
    path('update_orders/<int:id>', update_orders_view, name='update_orders'),
    path('delete_orders/<int:id>', delete_order_view, name='delete_orders')
]