# Generated by Django 2.1 on 2019-10-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebotapp', '0005_auto_20191012_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='svg_image',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
