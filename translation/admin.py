from django.contrib import admin
from .models import Course, BLog
# Register your models here.
admin.site.register(Course)

from parler.admin import TranslatableAdmin
admin.site.register(BLog, TranslatableAdmin)