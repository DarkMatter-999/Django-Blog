from django.contrib import admin

# Register your models here.

from .models import Author, Category, Post, Comment, Gallery

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Gallery)
#admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)