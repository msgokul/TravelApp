# Generated by Django 3.2.4 on 2021-06-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=250)),
                ('team_images', models.ImageField(upload_to='team_pics')),
                ('team_desc', models.TextField()),
            ],
        ),
    ]