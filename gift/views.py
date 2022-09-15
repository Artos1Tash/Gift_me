from rest_framework.viewsets import ModelViewSet
from gift.models import User, Room, Cart, Gift, News, Gift_image, Cart_product
from gift.serializers import UserSerializer, NewsSerializer, GiftSerializer, CartSerializer, RoomSerializer, \
    GiftImageSerializer, CartProductSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class GiftView(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartProductView(ModelViewSet):
    queryset =  Cart_product.objects.all()
    serializer_class = CartProductSerializer

class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GiftImageView(ModelViewSet):
    queryset = Gift_image.objects.all()
    serializer_class = GiftImageSerializer
