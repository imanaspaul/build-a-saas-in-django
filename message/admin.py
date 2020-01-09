from django.contrib import admin
from . models import Message , CountEmail


class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'owner']
    search_fields = ('owner',)


class CountAdmin(admin.ModelAdmin):
    list_display = ['owner', 'count']
    search_fields = ('owner',)


admin.site.register(Message, MessageAdmin)
admin.site.register(CountEmail, CountAdmin)