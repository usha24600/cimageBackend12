from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(userDetails)
admin.site.register(membershipDetails)
admin.site.register(eventDetails)
admin.site.register(registrationDetails)
