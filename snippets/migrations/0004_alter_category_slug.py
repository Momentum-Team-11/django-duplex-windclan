# Generated by Django 4.0.3 on 2022-03-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
