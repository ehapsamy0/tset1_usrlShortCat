# Generated by Django 2.2.6 on 2019-10-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20191025_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]