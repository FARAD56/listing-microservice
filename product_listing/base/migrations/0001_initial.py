# Generated by Django 5.0.6 on 2024-07-01 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('image', models.CharField(default='https://img.freepik.com/free-vector/shopping-cart-realistic_1284-6011.jpg?size=338&ext=jpg&ga=GA1.1.1141335507.1718064000&semt=ais_user', max_length=10000)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.region')),
            ],
        ),
    ]
