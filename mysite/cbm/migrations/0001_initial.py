# Generated by Django 2.2.2 on 2020-10-04 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('distributorname', models.CharField(db_column='DistributorName', max_length=10, primary_key=True, serialize=False)),
                ('distributortelephone', models.CharField(blank=True, db_column='DistributorTelephone', max_length=11, null=True)),
                ('storing', models.CharField(blank=True, db_column='Storing', max_length=20, null=True)),
            ],
            options={
                'db_table': 'distributor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('firmno', models.CharField(db_column='FirmNo', max_length=10, primary_key=True, serialize=False)),
                ('firmname', models.CharField(db_column='FirmName', max_length=10)),
                ('firmtelephone', models.CharField(blank=True, db_column='FirmTelephone', max_length=11, null=True)),
                ('firmemail', models.CharField(blank=True, db_column='FirmEmail', max_length=12, null=True)),
                ('firmaddress', models.CharField(blank=True, db_column='FirmAddress', max_length=20, null=True)),
            ],
            options={
                'db_table': 'firm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plantation',
            fields=[
                ('plantationno', models.CharField(db_column='PlantationNo', max_length=10, primary_key=True, serialize=False)),
                ('plantationname', models.CharField(db_column='PlantationName', max_length=10)),
                ('plantationtelephone', models.CharField(blank=True, db_column='PlantationTelephone', max_length=11, null=True)),
                ('plantationaddress', models.CharField(blank=True, db_column='PlantationAddress', max_length=20, null=True)),
            ],
            options={
                'db_table': 'plantation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productno', models.CharField(db_column='ProductNo', max_length=10, primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=10)),
                ('code', models.CharField(db_column='CODE', max_length=20)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('seedno', models.CharField(db_column='SeedNo', max_length=10, primary_key=True, serialize=False)),
                ('its1', models.CharField(db_column='ITS1', max_length=50)),
                ('its2', models.CharField(db_column='ITS2', max_length=50)),
                ('rcrrelf', models.CharField(db_column='RCRRELF', max_length=50)),
                ('species', models.CharField(blank=True, db_column='Species', max_length=5, null=True)),
                ('support', models.CharField(blank=True, db_column='Support', max_length=10, null=True)),
                ('origin', models.CharField(blank=True, db_column='Origin', max_length=10, null=True)),
            ],
            options={
                'db_table': 'seed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storename', models.CharField(db_column='StoreName', max_length=10, primary_key=True, serialize=False)),
                ('storetelephone', models.CharField(blank=True, db_column='StoreTelephone', max_length=11, null=True)),
                ('storeaddress', models.CharField(blank=True, db_column='StoreAddress', max_length=20, null=True)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plantationno', models.ForeignKey(db_column='PlantationNo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cbm.Plantation')),
                ('planting', models.DateTimeField(blank=True, db_column='Planting', null=True)),
            ],
            options={
                'db_table': 'plant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('plantationno', models.ForeignKey(db_column='PlantationNo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cbm.Plantation')),
                ('acquisition', models.DateTimeField(blank=True, db_column='Acquisition', null=True)),
                ('processing', models.CharField(blank=True, db_column='Processing', max_length=20, null=True)),
                ('packing', models.DateTimeField(blank=True, db_column='Packing', null=True)),
            ],
            options={
                'db_table': 'process',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provide',
            fields=[
                ('firmno', models.ForeignKey(db_column='FirmNo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cbm.Firm')),
                ('stock', models.DateTimeField(blank=True, db_column='Stock', null=True)),
            ],
            options={
                'db_table': 'provide',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('productno', models.ForeignKey(db_column='ProductNo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cbm.Product')),
                ('purchase', models.DateTimeField(blank=True, db_column='Purchase', null=True)),
            ],
            options={
                'db_table': 'sell',
                'managed': False,
            },
        ),
    ]
