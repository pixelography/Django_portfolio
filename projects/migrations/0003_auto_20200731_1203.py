# Generated by Django 3.0.8 on 2020-07-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200731_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(),
        ),
    ]
