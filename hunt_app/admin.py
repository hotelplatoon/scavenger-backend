from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Hunt)
admin.site.register(models.UserHunt)
admin.site.register(models.Checkpoint)