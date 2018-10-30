from django.contrib import admin
from .models import EchoUser,EchoUserSubmission,Problems

# Register your models here.
admin.site.register(EchoUser)
admin.site.register(EchoUserSubmission)
admin.site.register(Problems)