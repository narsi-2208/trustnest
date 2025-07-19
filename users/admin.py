from django.contrib import admin
from .models import Mentor, CareerSwitcher, User

admin.site.register(Mentor)
admin.site.register(CareerSwitcher)
admin.site.register(User)
admin.site.site_header = "BL-Task Admin"

