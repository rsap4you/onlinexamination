from django.contrib import admin
from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
