# Generated by Django 3.2.4 on 2022-02-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_auto_20210720_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
    ]
