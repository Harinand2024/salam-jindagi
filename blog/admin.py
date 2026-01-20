from django.contrib import admin
from .models import BlogPost, Category, Reporter, Tag, Comment


# ---------------- BLOG POST ----------------
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_cat', 'reporter', 'status', 'created_at')
    list_filter = ('status', 'post_cat', 'tags')
    search_fields = ('post_title',)
    prepopulated_fields = {"slug": ("post_title",)}
    filter_horizontal = ('tags',)


# ---------------- CATEGORY ----------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_slug')
    prepopulated_fields = {"cat_slug": ("cat_name",)}


# ---------------- TAG ----------------
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


# ---------------- REPORTER ----------------
@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('name',)


# ---------------- COMMENT ----------------
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'message')
