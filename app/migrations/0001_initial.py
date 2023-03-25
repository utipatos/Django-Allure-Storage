# Generated by Django 4.1.4 on 2023-02-17 10:57
import uuid

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllureResult',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
