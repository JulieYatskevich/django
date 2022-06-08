from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'date',
        'user',
    )


admin.site.register(Post)
