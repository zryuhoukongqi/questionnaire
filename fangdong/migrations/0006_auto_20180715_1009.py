# Generated by Django 2.0.7 on 2018-07-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fangdong', '0005_auto_20180714_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitors',
            name='degree',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='english_level',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
