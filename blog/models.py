from django.db import models
from django.utils.text import slugify

class Reporter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat_name


class BlogPost(models.Model):
    post_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    post_image = models.ImageField(upload_to='blogs/')
    description = models.TextField()

    reporter = models.ForeignKey(
        Reporter, on_delete=models.SET_NULL, null=True, blank=True
    )
    post_cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    schedule_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.post_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_title
