# Generated by Django 4.0.3 on 2022-03-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_snippet_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
