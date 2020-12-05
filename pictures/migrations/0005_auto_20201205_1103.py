# Generated by Django 3.1.2 on 2020-12-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_jpg_png'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='jpg',
            name='full_title',
        ),
        migrations.RemoveField(
            model_name='png',
            name='full_title',
        ),
        migrations.AddField(
            model_name='jpg',
            name='description',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='png',
            name='description',
            field=models.CharField(default='alma', max_length=64),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Extension',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
