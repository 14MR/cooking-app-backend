# Generated by Django 2.1.4 on 2019-07-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20190720_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipestep',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
