from django.contrib import admin
from .models import Catagory, Post ,Achievement ,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","catagory", "author", "created_on")
    list_filter = ('status', 'created_on','catagory')
    search_fields = ['title', 'catagory']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Catagory)
admin.site.register(Achievement)
admin.site.register(Comment,CommentAdmin)
