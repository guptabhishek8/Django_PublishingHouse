# Generated by Django 3.0.3 on 2020-03-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookApproved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/ApprovedPdfs/')),
                ('username', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
