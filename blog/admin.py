from django.contrib import admin
from .models import User,Experience,Education,skill,introduction

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('name','phonenumber','email','address')

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ('user','starttime','endtime','company','position')

class EducationAdmin(admin.ModelAdmin):
	list_display = ('user','starttime','endtime','school','content')

class skillAdmin(admin.ModelAdmin):
	list_display = ('user','skillname')

class introductionAdmin(admin.ModelAdmin):
	list_display = ('user','content')

admin.site.register(User,UserAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(skill,skillAdmin)
admin.site.register(introduction,introductionAdmin)