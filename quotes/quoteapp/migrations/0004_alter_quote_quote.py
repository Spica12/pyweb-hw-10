# Generated by Django 5.0.1 on 2024-01-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0003_remove_quote_created_remove_quote_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=300),
        ),
    ]
