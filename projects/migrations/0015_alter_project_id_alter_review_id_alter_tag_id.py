# Generated by Django 5.0 on 2024-01-15 09:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_project_id_alter_review_id_alter_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e86b0edd-ee0c-49a9-a66c-1afb66531e5e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('558e2884-e580-4046-ba67-04d6c2763edb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bc9aa23b-4b41-4d10-8dae-a9bf524be6cb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]