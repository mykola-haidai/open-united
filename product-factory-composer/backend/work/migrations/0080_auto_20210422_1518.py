# Generated by Django 3.1 on 2021-04-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0079_createproductrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createproductrequest',
            name='photo',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True),
        ),
    ]
