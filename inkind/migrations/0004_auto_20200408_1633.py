# Generated by Django 3.0.5 on 2020-04-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inkind', '0003_auto_20200408_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='hourly_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_value_of_service',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
