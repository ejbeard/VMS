# Generated by Django 2.1.7 on 2019-03-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190306_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_location',
            field=models.ManyToManyField(default='', related_name='related_userlocation', to='app.Map'),
        ),
    ]