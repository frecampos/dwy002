# Generated by Django 2.2.16 on 2020-10-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarW', '0002_auto_20201008_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderGaleria',
            fields=[
                ('ident', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='car')),
            ],
        ),
    ]
