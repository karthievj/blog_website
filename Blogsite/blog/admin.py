from django.contrib import admin
from .models import Profile,BlogPost,Comments

# Register your models here.

admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Comments)

