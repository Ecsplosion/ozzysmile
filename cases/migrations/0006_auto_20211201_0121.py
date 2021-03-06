# Generated by Django 3.2.5 on 2021-11-30 20:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0005_alter_case_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='bottom_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.AlterField(
            model_name='case',
            name='front_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.AlterField(
            model_name='case',
            name='general_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.AlterField(
            model_name='case',
            name='left_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.AlterField(
            model_name='case',
            name='right_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.AlterField(
            model_name='case',
            name='top_view',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'WMV'])]),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('date_posted', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('related_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.comment'),
        ),
    ]
