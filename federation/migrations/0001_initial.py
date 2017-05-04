# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confederation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confName', models.CharField(max_length=100, unique=True)),
                ('confAcronym', models.CharField(max_length=8, unique=True)),
                ('logo', models.CharField(max_length=250, unique=True)),
                ('confStrength', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=100, unique=True)),
                ('away', models.CharField(max_length=100, unique=True)),
                ('homeScore', models.IntegerField()),
                ('awayScore', models.IntegerField()),
                ('matchImportance', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('score', models.FloatField(blank=True, default=0.0, null=True)),
                ('flag', models.CharField(max_length=250, unique=True)),
                ('worldRanking', models.BooleanField(default=False)),
                ('confederationMembership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='federation.Confederation')),
            ],
        ),
    ]