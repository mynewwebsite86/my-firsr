from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_item'),
    path('increase/<int:item_id>/', views.increase_qty, name='increase_qty'),
    path('decrease/<int:item_id>/', views.decrease_qty, name='decrease_qty'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='orders'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('payment/', views.payment_page, name='payment'),
    path('my-products/', views.seller_products, name='my_products'),
    path('sell/', views.sell_product, name='sell_product'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('review/<int:product_id>/', views.add_review, name='add_review'),
    path("notifications/", views.notifications, name="notifications"),
    path("withdraw/", views.withdraw, name="withdraw"),
]

# create your urls here 