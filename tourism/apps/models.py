from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class City(models.Model):
    address = models.CharField(max_length=255, unique=True, null=True)
    description = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.address}"


class Tour(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    slug = models.CharField(max_length=255, null=True)
    tourCode = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to="static/images/avatar_tour", height_field=None, width_field=None,
                               max_length=255,
                               null=True, default="static/images/avatar_tour")
    firstImage = models.ImageField(upload_to="static/images/avatar_tour", height_field=None, width_field=None,
                                   max_length=255,
                                   null=True, default="static/images/avatar_tour")
    secondImage = models.ImageField(upload_to="static/images/avatar_tour", height_field=None, width_field=None,
                                    max_length=255,
                                    null=True, default="static/images/avatar_tour")
    thirdImage = models.ImageField(upload_to="static/images/avatar_tour", height_field=None, width_field=None,
                                   max_length=255,
                                   null=True, default="static/images/avatar_tour")
    price = models.FloatField(null=True)
    startingGate = models.ForeignKey(City, related_name="starting_gate", null=True, on_delete=models.CASCADE)
    destination = models.ForeignKey(City, related_name="destination", null=True, on_delete=models.CASCADE)
    starDay = models.DateField(null=True)
    endDate = models.DateField(null=True)
    maxQuantity = models.IntegerField(null=True)
    remaining = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"


class BookTour(models.Model):
    user = models.ForeignKey(User, related_name="booking_user", on_delete=models.CASCADE, null=True)
    tour = models.ForeignKey(Tour, related_name="booking_tour", on_delete=models.CASCADE, null=True)


class Blogs(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    avatar = models.ImageField(upload_to="static/images/image_blogs", height_field=None, width_field=None,
                               max_length=255,
                               null=True, default="static/images/image_blogs")
    firstImage = models.ImageField(upload_to="static/images/image_blogs", height_field=None, width_field=None,
                                   max_length=255,
                                   null=True, default="static/images/image_blogs")
    secondImage = models.ImageField(upload_to="static/images/image_blogs", height_field=None, width_field=None,
                                    max_length=255,
                                    null=True, default="static/images/image_blogs")
    thirdImage = models.ImageField(upload_to="static/images/image_blogs", height_field=None, width_field=None,
                                   max_length=255,
                                   null=True, default="static/images/image_blogs")
    city_blog = models.ForeignKey(City, related_name="city_blog", on_delete=models.CASCADE, null=True)
    description = models.TextField()
    description1 = models.TextField(null=True)
    description2 = models.TextField(null=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.city_blog, self.create_at)


class Comments(models.Model):
    blog = models.ForeignKey(Blogs, related_name="comments", on_delete=models.CASCADE, null=True)
    user_comment = models.ForeignKey(User, related_name="comments_name", on_delete=models.CASCADE, null=True)
    body_comment = models.TextField()
    date_comment = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.blog, self.user_comment, self.date_comment)
