# Generated by Django 4.0.3 on 2022-05-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocks', '0003_sabkoscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabkoscore',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
