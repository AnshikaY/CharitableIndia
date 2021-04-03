from django.contrib import admin
from . models import Donation, Membership, Feedback

# Register your models here.
admin.site.register(Donation)
admin.site.register(Membership)
admin.site.register(Feedback)