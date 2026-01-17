from blog.models import Category


def header_categories(request):
    return {
        "Blogcat": Category.objects.all()
    }
