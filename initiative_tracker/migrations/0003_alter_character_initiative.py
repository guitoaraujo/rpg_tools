# Generated by Django 5.1.6 on 2025-02-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative_tracker', '0002_alter_character_initiative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='initiative',
            field=models.IntegerField(default=0),
        ),
    ]
