# Generated by Django 5.0.1 on 2024-01-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_proxy', '0002_newsarticle_category_newsarticle_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='source_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='source_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]