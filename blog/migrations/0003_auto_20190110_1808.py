# Generated by Django 2.1.5 on 2019-01-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='address',
            field=models.CharField(default='www.google.com', max_length=255),
        ),
    ]
