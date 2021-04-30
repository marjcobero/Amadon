from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('purchase', views.purchase),
    path('checkout/<int:order_id>', views.checkout),
    path('new', views.new),
]
