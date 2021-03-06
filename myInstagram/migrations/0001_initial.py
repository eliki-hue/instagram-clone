# Generated by Django 4.0.3 on 2022-04-05 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, default='great', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('useremail', models.EmailField(max_length=20)),
                ('userage', models.CharField(max_length=2)),
                ('bio', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('user_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=60)),
                ('image_caption', models.CharField(max_length=100)),
                ('likes', models.CharField(blank=True, default=0, max_length=10)),
                ('comments', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myInstagram.comment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myInstagram.profile')),
            ],
        ),
    ]
