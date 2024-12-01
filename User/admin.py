from django.contrib import admin
from .models import Users

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "google_api_key"]
    list_filter = ["email"]
    search_fields = ['email']

admin.site.register(Users, UserAdmin)