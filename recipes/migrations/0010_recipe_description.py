# Generated by Django 2.1.4 on 2019-07-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_recipestep_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=None, max_length=300, null=True),
        ),
    ]