# Generated by Django 3.1 on 2021-06-15 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0084_user_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createproductrequest',
            old_name='created_by_person',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created_by_person',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='reviewer_person',
            new_name='reviewer',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='updated_by_person',
            new_name='updated_by',
        ),
    ]
