# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('createupdatebasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.CreateUpdateBaseModel')),
                ('display_name', models.CharField(max_length=30)),
                ('article_id', models.IntegerField()),
                ('content', models.TextField()),
                ('is_public', models.BinaryField(default=True)),
            ],
            options={
                'db_table': 'comment',
            },
            bases=('core.createupdatebasemodel',),
        ),
    ]
