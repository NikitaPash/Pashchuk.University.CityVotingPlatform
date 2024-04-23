# Generated by Django 5.0.3 on 2024-04-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField()),
                ('administration', models.CharField(max_length=200)),
                ('administration_contact', models.CharField(max_length=100)),
            ],
        ),
    ]
