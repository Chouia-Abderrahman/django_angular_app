# Generated by Django 5.0.1 on 2024-01-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=255)),
                ('source_name', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(unique=True)),
                ('url_to_image', models.URLField(blank=True, null=True)),
                ('published_at', models.DateTimeField()),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
