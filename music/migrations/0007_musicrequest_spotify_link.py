# Generated by Django 5.0.6 on 2024-07-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_musicrequest_item_image_url_musicrequest_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicrequest',
            name='spotify_link',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
