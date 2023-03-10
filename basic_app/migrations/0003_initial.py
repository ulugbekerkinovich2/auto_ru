# Generated by Django 4.1.6 on 2023-02-10 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic_app', '0002_remove_model1_mark_name_delete_mark_delete_model1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_name', models.CharField(default=None, max_length=500, unique=True)),
            ],
            options={
                'db_table': 'mark',
            },
        ),
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='none', max_length=500)),
                ('mark_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.mark', verbose_name='mark_name')),
            ],
            options={
                'db_table': 'model1',
            },
        ),
    ]
