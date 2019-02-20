# Generated by Django 2.1.4 on 2019-02-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='profile_pic',
            field=models.ImageField(default='media_data/profile-pic.png', upload_to='host_data'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='media_data/profile-pic.png', upload_to='user_data'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='profile_pic',
            field=models.ImageField(default='media_data/profile-pic.png', upload_to='visitor_data'),
        ),
    ]
