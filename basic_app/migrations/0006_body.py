# Generated by Django 4.1.6 on 2023-02-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_of_vehicle', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'body',
            },
        ),
    ]
