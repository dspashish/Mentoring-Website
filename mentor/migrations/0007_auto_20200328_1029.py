# Generated by Django 2.1 on 2020-03-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0006_discuss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discuss',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
