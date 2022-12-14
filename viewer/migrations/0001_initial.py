# Generated by Django 3.0 on 2022-10-20 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('color', models.CharField(max_length=18)),
                ('URL', models.CharField(max_length=128)),
                ('album_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.Album')),
            ],
        ),
    ]
