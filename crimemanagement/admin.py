from django.contrib import admin
from .models import Auth,Complaint,Crime
# Register your models here.
admin.site.register(Auth)
admin.site.register(Complaint)
admin.site.register(Crime)
