from django.contrib import admin

from .models import City, Tour, BookTour, Blogs, Comments

# Register your models here.

admin.site.register(City)
admin.site.register(Tour)
admin.site.register(Blogs)
admin.site.register(Comments)



