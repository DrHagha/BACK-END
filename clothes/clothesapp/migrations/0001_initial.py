# Generated by Django 3.0.8 on 2022-06-29 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('heart', models.IntegerField()),
            ],
        ),
    ]
