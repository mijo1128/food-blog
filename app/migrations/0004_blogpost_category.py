# Generated by Django 4.1.7 on 2023-03-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_rename_post_author_blogpost_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.CharField(
                choices=[
                    ("Entree", "Entree"),
                    ("Appetizer", "Appetizer"),
                    ("Dessert", "Dessert"),
                    ("Cocktail", "Cocktail"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
