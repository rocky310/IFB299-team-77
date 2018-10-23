# Generated by Django 2.1.1 on 2018-10-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Hyundai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Kia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Mitsubishi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Toyota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]