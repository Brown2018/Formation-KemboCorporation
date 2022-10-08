from django.contrib import admin

# Register your models here.
from .models import Services, Equipe,Model_Message

admin.site.register(Services)
admin.site.register(Equipe)
admin.site.register(Model_Message)