# Generated by Django 3.1.5 on 2021-01-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
