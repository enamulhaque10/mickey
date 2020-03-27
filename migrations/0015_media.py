# Generated by Django 3.0.4 on 2020-03-27 04:34

import dblog.files
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dblog', '0014_auto_20200327_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cover_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/blog/images/'), upload_to=dblog.files.cover_image_upload_path, verbose_name='Cover Image')),
                ('m_cover_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/blog/images/'), upload_to=dblog.files.m_cover_image_upload_path, verbose_name='Medium Cover Image')),
                ('sm_cover_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/blog/images/'), upload_to=dblog.files.sm_cover_image_upload_path, verbose_name='Small Cover Image')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dblog_media_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dblog_media_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
