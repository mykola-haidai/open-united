# Generated by Django 3.1 on 2021-06-15 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0009_user_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskclaim',
            old_name='customer_person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='taskclaimrequest',
            old_name='customer_person',
            new_name='person',
        ),
    ]
