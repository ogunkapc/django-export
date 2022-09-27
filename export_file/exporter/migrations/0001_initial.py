# Generated by Django 4.0.6 on 2022-07-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.TextField(db_column='description')),
                ('author', models.CharField(db_column='author', max_length=100)),
                ('year', models.IntegerField(db_column='year', default=2000)),
            ],
        ),
    ]
