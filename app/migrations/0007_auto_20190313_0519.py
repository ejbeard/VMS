# Generated by Django 2.1.7 on 2019-03-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'secretary'), ('2', 'receptionist'), ('3', 'admin')], default='', max_length=20),
        ),
    ]