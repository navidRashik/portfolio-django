# Generated by Django 2.2 on 2019-04-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publication_date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
