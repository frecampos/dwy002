# Generated by Django 2.2.16 on 2020-10-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarW', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderindex',
            name='ident',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
