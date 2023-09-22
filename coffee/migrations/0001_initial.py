# Generated by Django 4.2.5 on 2023-09-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=60)),
                ('giftTo', models.TextField(blank=True)),
                ('time', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'coffee',
            },
        ),
    ]
