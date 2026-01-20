from django.db import models


class Reporter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    post_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    post_cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    reporter = models.ForeignKey(        # ✅ FIXED
        Reporter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    description = models.TextField()
    post_image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    blog = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name
