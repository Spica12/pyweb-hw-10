# Generated by Django 5.0.1 on 2024-01-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0009_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=1000),
        ),
    ]
