# Generated by Django 2.2.4 on 2019-09-11 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
                ('prict', models.FloatField()),
                ('describe', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', models.CharField(max_length=32)),
                ('a_price', models.FloatField()),
                ('u_name', models.CharField(max_length=32)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commodity')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
