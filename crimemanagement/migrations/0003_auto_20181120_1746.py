# Generated by Django 2.1.3 on 2018-11-20 12:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('crimemanagement', '0002_complaint_status'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='complaint',
            managers=[
                ('crime', django.db.models.manager.Manager()),
            ],
        ),
    ]