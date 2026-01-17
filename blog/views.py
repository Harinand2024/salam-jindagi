from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category   # ✅ Capital C

def blog_list(request):
    blogs = BlogPost.objects.filter(status=True)
    return render(request, "blog.html", {
        "blogs": blogs
    })


def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, status=True)

    Blogcat = Category.objects.all()   # ya filter agar chaho

    return render(request, "blog_detail.html", {
        "blog": blog,
        "Blogcat": Blogcat,
    })
