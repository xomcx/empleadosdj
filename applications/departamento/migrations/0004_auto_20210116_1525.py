# Generated by Django 3.1.4 on 2021-01-16 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20210116_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='short_name',
            new_name='shor_name',
        ),
    ]
