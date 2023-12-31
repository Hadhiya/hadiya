# Generated by Django 4.2.7 on 2023-11-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_amount', models.IntegerField()),
                ('item_id', models.IntegerField(default=0)),
                ('username', models.CharField(default='default_username', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField()),
                ('item_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_mas_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('odate', models.IntegerField()),
                ('grand_total', models.IntegerField()),
                ('u_address', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50)),
                ('u_address', models.CharField(max_length=150)),
                ('u_place', models.CharField(max_length=100)),
                ('u_contact', models.IntegerField()),
                ('u_email', models.TextField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
