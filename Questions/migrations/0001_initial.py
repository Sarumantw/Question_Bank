# Generated by Django 5.1.5 on 2025-01-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('correct', models.CharField(max_length=1)),
            ],
        ),
    ]
