# Generated by Django 4.2.5 on 2023-10-04 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True, unique=True)),
                ('description', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('slug', models.CharField(max_length=255, null=True)),
                ('tourCode', models.CharField(max_length=255, null=True)),
                ('avatar', models.ImageField(default='static/images/avatar_tour', max_length=255, null=True, upload_to='static/images/avatar_tour')),
                ('firstImage', models.ImageField(default='static/images/avatar_tour', max_length=255, null=True, upload_to='static/images/avatar_tour')),
                ('secondImage', models.ImageField(default='static/images/avatar_tour', max_length=255, null=True, upload_to='static/images/avatar_tour')),
                ('thirdImage', models.ImageField(default='static/images/avatar_tour', max_length=255, null=True, upload_to='static/images/avatar_tour')),
                ('price', models.FloatField(null=True)),
                ('starDay', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('maxQuantity', models.IntegerField(null=True)),
                ('remaining', models.IntegerField(null=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='apps.city')),
                ('startingGate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starting_gate', to='apps.city')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('price', models.FloatField()),
                ('avatar', models.ImageField(default='static/images/hotel_img', max_length=255, null=True, upload_to='static/images/hotel_img')),
                ('firstImage', models.ImageField(default='static/images/hotel_img', max_length=255, null=True, upload_to='static/images/hotel_img')),
                ('secondImage', models.ImageField(default='static/images/hotel_img', max_length=255, null=True, upload_to='static/images/hotel_img')),
                ('thirdImage', models.ImageField(default='static/images/hotel_img', max_length=255, null=True, upload_to='static/images/hotel_img')),
                ('numberRemainingRoom', models.IntegerField(null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_hotel', to='apps.city')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=12, null=True, unique=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Contact_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_tour', to='apps.tour')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to='apps.customer')),
            ],
        ),
    ]