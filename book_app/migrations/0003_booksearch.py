# Generated by Django 3.2.9 on 2021-12-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_auto_20211203_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
    ]