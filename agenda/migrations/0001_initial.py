# Generated by Django 2.2.4 on 2019-10-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
    ]