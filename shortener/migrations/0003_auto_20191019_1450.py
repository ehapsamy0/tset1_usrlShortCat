# Generated by Django 2.2.6 on 2019-10-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kirrurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
