from django.contrib import admin
from .models import BlogPost, Category, Reporter

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_cat', 'reporter', 'status')
    prepopulated_fields = {'slug': ('post_title',)}
    list_filter = ('status', 'post_cat')
    search_fields = ('post_title',)


admin.site.register(Category)
admin.site.register(Reporter)
