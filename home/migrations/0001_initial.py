# Generated by Django 2.2 on 2020-03-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('service', models.CharField(max_length=200, verbose_name='service')),
                ('barder', models.CharField(max_length=200, verbose_name='barder')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('date', models.CharField(max_length=200, verbose_name='date')),
                ('time', models.CharField(max_length=200, verbose_name='time')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('img', models.ImageField(upload_to='image_product', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('detail', models.CharField(max_length=200, verbose_name='detail')),
                ('state', models.BooleanField(default=True, verbose_name='state')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
