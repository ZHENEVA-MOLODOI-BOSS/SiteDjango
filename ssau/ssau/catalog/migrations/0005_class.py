# Generated by Django 5.0.4 on 2024-04-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_time_pair_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_class', models.CharField(help_text='Введите номер аудитории', max_length=12)),
            ],
        ),
    ]
