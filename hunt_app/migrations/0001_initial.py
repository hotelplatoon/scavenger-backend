# Generated by Django 2.1.3 on 2019-04-13 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('checkpoint_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCheckpointImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=255)),
                ('checkpoint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkpoints', to='hunt_app.Checkpoint')),
            ],
        ),
        migrations.CreateModel(
            name='UserHunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('hunt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunts', to='hunt_app.Hunt')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usercheckpointimage',
            name='user_hunt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userhunts', to='hunt_app.UserHunt'),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='hunt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunt', to='hunt_app.Hunt'),
        ),
    ]
