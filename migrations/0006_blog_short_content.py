# Generated by Django 3.0.4 on 2020-03-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0005_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_content',
            field=models.TextField(blank=True, null=True, verbose_name='Short Content'),
        ),
    ]
