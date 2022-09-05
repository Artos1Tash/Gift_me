from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     email = models.EmailField(max_length=200)
#     date_of_birth = models.DateTimeField()
#     about_user = models.TextField(max_length=140)
#     social_network = models.URLField(max_length=300)
#
#     def __str__(self):
#         return f'{self.name}'


class Gift(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='gift')

    def __str__(self):
        return f'{self.name}'

class Gift_image(models.Model):
    image = models.URLField()
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='gift_image')

    def __str__(self):
        return f'{self.name}'

class News(models.Model):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='poster')

    def __str__(self):
        return f'{self.name}'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    user_that_get_gift = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='recipient')
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='giftt')


    def __str__(self):
        return f'{self.name}'

class Room(models.Model):
    info = models.TextField(max_length=500)
    user_friends = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='friends')
    list_of_gifts = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True, related_name='wish')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_room')
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True, related_name='news')


    def __str__(self):
        return f'{self.name}'
