# Generated by Django 3.0.6 on 2020-05-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0005_auto_20200510_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='styles',
            field=models.ManyToManyField(blank=True, related_name='beers', to='beers.BeerStyle'),
        ),
    ]