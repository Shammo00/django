# Generated by Django 5.1.2 on 2024-11-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0012_alter_entry_image_alter_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
