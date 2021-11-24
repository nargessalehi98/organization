from django.contrib import admin
from . import models

admin.site.register(models.employee)
admin.site.register(models.manager)
admin.site.register(models.organization)
admin.site.register(models.RequestForManagement)
admin.site.register(models.RequestForMembership)
admin.site.register(models.task)