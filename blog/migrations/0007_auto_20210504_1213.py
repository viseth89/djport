# Generated by Django 3.2 on 2021-05-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210504_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title1',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title2',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title3',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title4',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
