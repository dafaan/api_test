# Generated by Django 3.2.15 on 2022-12-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etapp', '0004_rename_cod_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(blank=True, default='', max_length=6, null=True),
        ),
    ]
