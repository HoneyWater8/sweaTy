# Generated by Django 5.0.3 on 2024-03-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0005_testmodel_cnt_alter_testmodel_label_0_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='cnt',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='squatAccuracy',
            field=models.CharField(default='-1', max_length=5),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='squatBeforeState',
            field=models.CharField(default='1', max_length=5),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='squatCnt',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='squatNowState',
            field=models.CharField(default='1', max_length=5),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='squatState',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='stateQueue',
            field=models.CharField(default='nnnnn', max_length=5),
        ),
    ]