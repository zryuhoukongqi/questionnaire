# Generated by Django 2.0.7 on 2018-07-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fangdong', '0004_auto_20180714_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitrecords',
            name='question1_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='question2_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='question3_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='question4_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='question5_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='question6_score',
            field=models.IntegerField(default=0),
        ),
    ]
