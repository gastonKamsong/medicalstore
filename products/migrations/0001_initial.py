# Generated by Django 5.2.4 on 2025-07-18 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('meta_description', models.CharField(blank=True, help_text='SEO meta description', max_length=160)),
                ('meta_keywords', models.CharField(blank=True, help_text='SEO keywords', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(help_text='Rich text description of the product')),
                ('composition', models.TextField(help_text='Key elements or ingredients')),
                ('usage_instructions', models.TextField(help_text='How to use this product')),
                ('creation_method', models.TextField(help_text='How it is produced or formulated')),
                ('benefits', models.TextField(help_text='Health benefits')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('meta_description', models.CharField(blank=True, help_text='SEO meta description', max_length=160)),
                ('meta_keywords', models.CharField(blank=True, help_text='SEO keywords', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False, help_text='Show on homepage')),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['slug'], name='products_pr_slug_3edc0c_idx'), models.Index(fields=['category', 'is_active'], name='products_pr_categor_50f5f1_idx'), models.Index(fields=['featured', 'is_active'], name='products_pr_feature_80c52d_idx')],
            },
        ),
    ]
