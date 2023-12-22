from django.contrib import admin

from .models import *

class ReceipeAdmin(admin.ModelAdmin):
	list_display = ['receipe_name','receipe_discription','receipe_image']
#readonly_fields = ('image_tag',)

admin.site.register(Receipe,ReceipeAdmin)
