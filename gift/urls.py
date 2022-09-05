from django.contrib import admin
from django.urls import path
from gift.views import UserView, GiftView, NewsView, RoomView, CartView, GiftImageView

urlpatterns = [
    path('user/', UserView.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('gift/', GiftView.as_view({'get': 'list', 'post': 'create'})),
    path('gift/<int:pk>/', GiftView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('news/', NewsView.as_view({'get': 'list', 'post': 'create'})),
    path('news/<int:pk>/', NewsView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('room/', RoomView.as_view({'get': 'list', 'post': 'create'})),
    path('room/<int:pk>/', RoomView.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('cart/', CartView.as_view({'get': 'list', 'post': 'create'})),
    path('cart/<int:pk>/', CartView.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('gift_image/', GiftImageView.as_view({'get': 'list'})),
    path('gift_image/<int:pk>/', GiftImageView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))

]
