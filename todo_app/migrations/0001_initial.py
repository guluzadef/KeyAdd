# Generated by Django 3.0.3 on 2020-02-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SSH', 'SSH'), ('FTB', 'FTB'), ('ADMIN', 'ADMIN'), ('EMAIL', 'EMAIL')], default='SSH', max_length=255)),
                ('host', models.CharField(max_length=12)),
                ('port', models.IntegerField()),
                ('user', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
