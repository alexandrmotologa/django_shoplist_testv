# Generated by Django 3.1.1 on 2020-09-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200919_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='cover.png', upload_to='cover'),
        ),
    ]
