# Generated by Django 5.0.7 on 2024-07-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
