# Generated by Django 3.0.3 on 2020-02-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200226_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='username',
            field=models.CharField(default='asd', max_length=100),
        ),
    ]
