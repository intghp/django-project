# Generated by Django 5.1.1 on 2024-09-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=50)),
            ],
        ),
    ]
