from .models import BlogPost, Category

def global_context(request):
    return {
        "Blogcat": Category.objects.all().order_by('id'),
        "recent_posts": BlogPost.objects.filter(
            status=True
        ).order_by('-id')[:3],
    }
