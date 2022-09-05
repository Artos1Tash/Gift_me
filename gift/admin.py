from django.contrib import admin
from gift.models import Gift, User, Room, News, Cart, Gift_image


admin.site.register(Gift)
admin.site.register(Room)
admin.site.register(News)
admin.site.register(Cart)
admin.site.register(Gift_image)

