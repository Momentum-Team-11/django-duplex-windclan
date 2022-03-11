from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Snippet(models.Model):
    title = models.CharField(max_length=500)
    language = models.CharField(max_length=100)
    category = models.ManyToManyField("Category", related_name="snippets", blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, null=True, related_name="snippets")
    # favorite = models.ManyToManyField("user", related_name="favorite_snippets")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()