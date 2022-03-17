from turtle import onclick
from unicodedata import category
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from PIL import Image


class CustomUser(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

languages = [
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('Django', 'Django')
]

class Snippet(models.Model):
    title = models.CharField(max_length=500)
    language = models.CharField(choices=languages, max_length=20, blank=True, null=True)
    category = models.ManyToManyField("Category", related_name="snippets", blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    code = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="snippets")
    public = models.BooleanField(default=False)
    og_snippet = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="snippet_copies",)
    copy_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/')
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()