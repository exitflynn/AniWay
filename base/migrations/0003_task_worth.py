# Generated by Django 4.0.1 on 2022-01-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210322_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='worth',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]