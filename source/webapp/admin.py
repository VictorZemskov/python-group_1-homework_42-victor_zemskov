from django.contrib import admin
from webapp.models import User, Article

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_vertical = ('favorites',)

admin.site.register(User, UserAdmin)
admin.site.register(Article)