# Generated by Django 5.1.2 on 2024-11-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_alter_entry_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]