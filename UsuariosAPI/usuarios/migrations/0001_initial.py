# Generated by Django 2.1.1 on 2018-10-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(default='', max_length=45)),
                ('apellidos', models.CharField(default='', max_length=45)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]