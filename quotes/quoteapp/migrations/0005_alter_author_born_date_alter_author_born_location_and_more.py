# Generated by Django 5.0.1 on 2024-01-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0004_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
