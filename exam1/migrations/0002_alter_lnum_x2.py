# Generated by Django 4.1.1 on 2022-09-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnum',
            name='x2',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
