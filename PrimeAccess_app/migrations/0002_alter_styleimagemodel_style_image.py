# Generated by Django 3.2.12 on 2022-07-13 12:01

import PrimeAccess_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeAccess_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styleimagemodel',
            name='style_image',
            field=models.ImageField(upload_to=PrimeAccess_app.models.StylePhotoRename),
        ),
    ]
