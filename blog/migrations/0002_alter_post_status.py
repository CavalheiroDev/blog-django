# Generated by Django 3.2.8 on 2021-10-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Rascunho'), (1, 'Publicar')], default=0),
        ),
    ]
