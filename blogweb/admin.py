from django.contrib import admin
from .models import Post, contact
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")


admin.site.register(Post, PostAdmin),
