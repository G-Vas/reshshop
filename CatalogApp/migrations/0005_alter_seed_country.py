# Generated by Django 3.2.1 on 2021-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogApp', '0004_alter_seed_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='country',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
    ]
