# Generated by Django 3.1.3 on 2020-11-16 03:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201116_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sonotakenpin',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')], verbose_name='その他検品'),
        ),
    ]
