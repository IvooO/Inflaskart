# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 20:49
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocerystore', '0002_auto_20170510_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(auto_now_add=True), size=None)),
                ('nb_of_purchases', models.PositiveIntegerField(default=1)),
                ('bought_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocerystore.Product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['customer__username', 'bought_product__product_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'ordering': ['parent__top_category', 'sub_category_name'], 'verbose_name': 'product sub-category', 'verbose_name_plural': 'product sub-categories'},
        ),
    ]