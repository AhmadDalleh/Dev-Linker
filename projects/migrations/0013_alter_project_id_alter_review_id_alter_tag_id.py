# Generated by Django 5.0 on 2024-01-02 13:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_project_id_alter_review_id_alter_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a3c485da-ceba-4edc-a1b7-8e4bdec733f7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d38dae4b-3e99-4e7f-9b26-6d3e182ec7b4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('757bc64b-2920-4a20-83ac-73b2514ddb67'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
