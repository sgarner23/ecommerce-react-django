# Generated by Django 4.0.1 on 2022-01-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test_name',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
    ]