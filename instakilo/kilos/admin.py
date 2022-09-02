from django.contrib import admin
from .models import userprofile,profilepost,comment
# Register your models here.


@admin.register(userprofile)
class adminuserprofile(admin.ModelAdmin):
    list_display = ["user","accountcreated"]

admin.site.register(profilepost)
admin.site.register(comment)