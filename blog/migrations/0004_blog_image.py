# Generated by Django 2.2 on 2019-04-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190424_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='exit', upload_to='images/', verbose_name='image input'),
            preserve_default=False,
        ),
    ]