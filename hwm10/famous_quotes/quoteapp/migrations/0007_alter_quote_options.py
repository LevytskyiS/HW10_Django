# Generated by Django 4.1.7 on 2023-02-19 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0006_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ['time_create'], 'verbose_name': 'Famous quote', 'verbose_name_plural': 'Famous quotes'},
        ),
    ]