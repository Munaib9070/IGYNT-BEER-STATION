# Generated by Django 5.0.3 on 2024-03-22 07:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]
