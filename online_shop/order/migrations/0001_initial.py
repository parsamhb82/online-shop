# Generated by Django 5.1 on 2024-08-27 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='code must be unique and less than 10 characters', max_length=16, unique=True)),
                ('percentage', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='code must be unique and less than 10 characters', max_length=16, unique=True)),
                ('is_received', models.BooleanField(default=False)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cart.cart')),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.costumer')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.discount')),
                ('products', models.ManyToManyField(blank=True, to='product.product')),
            ],
        ),
    ]
