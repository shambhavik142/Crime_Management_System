# Generated by Django 2.1.3 on 2018-11-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaintnumber', models.IntegerField(max_length=5)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=6)),
                ('date', models.DateField(max_length=10)),
                ('mail', models.EmailField(max_length=256)),
                ('pno', models.IntegerField(max_length=10)),
                ('add', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crimenumber', models.IntegerField(max_length=5)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('crime', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=2)),
            ],
        ),
    ]