# Generated by Django 5.1.1 on 2024-09-27 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='senha',
        ),
    ]
