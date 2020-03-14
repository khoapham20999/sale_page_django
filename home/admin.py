from django.contrib import admin

# Register your models here.

from home.models import product, user, appointment, post

admin.site.register(product)
admin.site.register(user)
admin.site.register(appointment)
admin.site.register(post)
