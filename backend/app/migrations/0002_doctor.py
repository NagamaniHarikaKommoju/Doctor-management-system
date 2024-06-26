# Generated by Django 5.0.3 on 2024-05-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('languages', models.CharField(max_length=200)),
            ],
        ),
    ]
