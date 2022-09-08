from rest_framework import serializers
from gift.models import User, Cart, Gift, News, Gift_image, Room, Cart_product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GiftImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift_image
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart_product
        fields = '__all__'
