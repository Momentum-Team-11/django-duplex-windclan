# Generated by Django 4.0.3 on 2022-03-17 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_snippet_og_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
