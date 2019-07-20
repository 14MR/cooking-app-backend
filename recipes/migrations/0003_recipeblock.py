# Generated by Django 2.1.4 on 2019-07-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20190720_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', 'image'), ('text', 'text'), ('timer', 'timer')], max_length=100)),
                ('step', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='recipes.RecipeStep')),
            ],
        ),
    ]
