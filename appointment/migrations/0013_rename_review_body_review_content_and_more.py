# Generated by Django 4.2.2 on 2023-06-28 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0012_rename_reviews_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='name_review',
            new_name='reviewer',
        ),
    ]
