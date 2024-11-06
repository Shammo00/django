from django.contrib import admin

# Register your models here.
from  .models import text , Topic , Entry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(text)