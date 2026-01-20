from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import BlogPost, Category, Tag, Comment
# =========================
# BLOG LIST
# =========================
def blog_list(request):
    blogs_qs = BlogPost.objects.filter(status=True).order_by('-created_at')

    paginator = Paginator(blogs_qs, 6)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'blogs.html', {
        'blogs': blogs
    })

# =========================
# BLOG DETAIL + COMMENT
# =========================
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, status=True)

    categories = Category.objects.all()

    recent_posts = BlogPost.objects.filter(
        status=True
    ).exclude(id=blog.id).order_by('-created_at')[:3]

    next_blog = BlogPost.objects.filter(
        status=True,
        created_at__gt=blog.created_at
    ).order_by('created_at').first()

    prev_blog = BlogPost.objects.filter(
        status=True,
        created_at__lt=blog.created_at
    ).order_by('-created_at').first()

    if request.method == 'POST':
        Comment.objects.create(
            blog=blog,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return redirect(request.path)

    context = {
        'blog': blog,
        'categories': categories,
        'recent_posts': recent_posts,
        'next_blog': next_blog,
        'prev_blog': prev_blog,
    }

    return render(request, 'blog_detail.html', context)


# =========================
# TAG WISE BLOGS
# =========================
def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    blogs = BlogPost.objects.filter(
        tags=tag,
        status=True
    ).order_by('-created_at')

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, 'blogs.html', {
        'blogs': blogs,
        'tag': tag
    })


# =========================
# CATEGORY WISE BLOGS
# =========================
def category_blogs(request, slug):
    category = get_object_or_404(Category, cat_slug=slug)

    blogs = BlogPost.objects.filter(
        post_cat=category,
        status=True
    ).order_by('-created_at')

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, 'blogs.html', {
        'blogs': blogs,
        'current_category': category
    })
