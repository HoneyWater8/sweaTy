# Generated by Django 5.0.3 on 2024-03-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0008_alter_testmodel_statequeue'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='classIdx',
            field=models.CharField(default='-1', max_length=50),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='squatAccuracy',
            field=models.CharField(default='-1', max_length=10),
        ),
    ]
