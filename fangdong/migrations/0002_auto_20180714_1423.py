# Generated by Django 2.0.7 on 2018-07-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fangdong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='visitors',
            name='visitor_Landlord',
        ),
        migrations.AlterField(
            model_name='landlord',
            name='response_rate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='landlord_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fangdong.Landlord'),
        ),
        migrations.AddField(
            model_name='visitrecords',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fangdong.Visitors'),
        ),
    ]
