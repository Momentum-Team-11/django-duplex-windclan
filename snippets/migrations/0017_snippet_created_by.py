# Generated by Django 4.0.3 on 2022-03-17 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_merge_20220317_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]