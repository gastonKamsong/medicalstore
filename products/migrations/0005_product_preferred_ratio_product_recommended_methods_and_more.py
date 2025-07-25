# Generated by Django 5.2.4 on 2025-07-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_category_preferred_ratio_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="preferred_ratio",
            field=models.CharField(
                blank=True,
                choices=[
                    ("high_cbd", "High CBD (20:1)"),
                    ("balanced", "Balanced (1:1)"),
                    ("high_thc", "High THC (1:20)"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="recommended_methods",
            field=models.JSONField(
                blank=True, help_text="e.g., ['flower', 'oil']", null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="strain_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Sativa", "Sativa"),
                    ("Indica", "Indica"),
                    ("Hybrid", "Hybrid"),
                    ("Other", "Other"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
