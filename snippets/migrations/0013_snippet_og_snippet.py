# Generated by Django 4.0.3 on 2022-03-17 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_snippet_copy_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='og_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_copies', to='snippets.snippet'),
        ),
    ]
