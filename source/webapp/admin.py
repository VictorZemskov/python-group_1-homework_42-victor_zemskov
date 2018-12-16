from django.contrib import admin
from webapp.models import User, Article, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_vertical = ('favorites',)

admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Comment)