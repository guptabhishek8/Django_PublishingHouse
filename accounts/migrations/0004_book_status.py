# Generated by Django 3.0.3 on 2020-03-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='Pending', max_length=100, null=True),
        ),
    ]
