# Generated by Django 3.0.3 on 2020-02-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='port',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='type',
            field=models.CharField(choices=[('SSH', 'SSH'), ('FTB', 'FTB'), ('ADMIN', 'ADMIN'), ('EMAIL', 'EMAIL')], default='ADMIN', max_length=255),
        ),
    ]