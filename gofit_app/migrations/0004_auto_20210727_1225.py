# Generated by Django 3.1.7 on 2021-07-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gofit_app', '0003_auto_20210722_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motioninfo',
            name='motion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]