# Generated by Django 3.2.1 on 2021-05-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogApp', '0003_alter_seed_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='purpose',
            field=models.CharField(default='Выращивание в горшке или открытом грунте', max_length=100, verbose_name='Предназначение'),
        ),
    ]