# Generated by Django 2.1 on 2020-03-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='std',
            field=models.IntegerField(blank=True, max_length=200),
        ),
    ]
