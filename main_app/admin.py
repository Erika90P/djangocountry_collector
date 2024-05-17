from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Country

from .models import Holidays
from .models import Rivers

# Register your models here
admin.site.register(Country)

admin.site.register(Holidays)

admin.site.register(Rivers)