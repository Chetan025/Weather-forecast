# Generated by Django 2.2.2 on 2019-07-24 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20190724_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['id'], 'verbose_name_plural': 'cities'},
        ),
    ]