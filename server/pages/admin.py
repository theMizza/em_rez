from django.contrib import admin
from .models import StaticPages, ImageGroups, Images, TextBlocks
# Register your models here.

admin.site.register(StaticPages)
admin.site.register(ImageGroups)
admin.site.register(Images)
admin.site.register(TextBlocks)
