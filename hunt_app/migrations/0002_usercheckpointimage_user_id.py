# Generated by Django 2.1.3 on 2019-04-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercheckpointimage',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
