# Generated by Django 5.0.3 on 2024-03-28 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_rename_text_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comment_text',
        ),
    ]