# Generated by Django 2.1 on 2019-10-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebotapp', '0002_auto_20191005_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='sub_category',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]