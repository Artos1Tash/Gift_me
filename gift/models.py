from django.contrib.auth.models import User
from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='gift')

    def __str__(self):
        return f'{self.name}'

class Gift_image(models.Model):
    image = models.URLField()
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='gift_image')

    def __str__(self):
        return f'{self.gift}'

class News(models.Model):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='poster')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    user_that_get_gift = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='recipient')
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='giftt')

    def __str__(self):
        return f'{self.user.first_name}'

class Cart_product(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True, related_name='cart_id')
    product_id = models.ForeignKey(Gift, on_delete=models.CASCADE, blank=True, null=True, related_name='product_id')

class Room(models.Model):
    info = models.TextField(max_length=500)
    user_friends = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='friends')
    list_of_gifts = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='wish')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_room')
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True, related_name='news')


    def __str__(self):
        return f'{self.user_friends} room created succesfully'
