# Generated by Django 2.2.16 on 2020-10-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarW', '0005_insumos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumos',
            name='ident',
        ),
        migrations.AlterField(
            model_name='insumos',
            name='nombre',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
