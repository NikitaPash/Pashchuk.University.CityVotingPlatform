# Generated by Django 5.0.3 on 2024-03-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_alter_vote_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
    ]