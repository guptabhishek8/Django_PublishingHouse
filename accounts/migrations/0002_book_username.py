# Generated by Django 3.0.3 on 2020-02-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
