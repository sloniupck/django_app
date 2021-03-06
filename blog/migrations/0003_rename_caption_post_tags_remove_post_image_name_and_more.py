# Generated by Django 4.0.3 on 2022-04-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(max_length=150),
        ),
    ]
