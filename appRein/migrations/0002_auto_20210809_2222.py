# Generated by Django 3.2.4 on 2021-08-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRein', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='imagen',
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagenperfil',
            field=models.ImageField(blank=True, null=True, upload_to='foro'),
        ),
    ]
