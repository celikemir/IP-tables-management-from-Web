# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import *

# Register your models here.

class ChainAdmin(admin.ModelAdmin):
    list_display = ['chain_name']
    search_fields = ['chain_name']
    class Meta:
        model = Chain

class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['protocol_name']
    search_fields = ['protocol_name']
    class Meta:
        model = Protocol

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_port']
    search_fields = ['service_name', 'service_port']
    class Meta:
        model = Service

class RuleAdmin(admin.ModelAdmin):
    list_display = ['chain', 'protocol', 'source_port', 'destination_port', 'source_ip', 'destination_ip', 'operation', 'is_run']
    list_filter = ['is_run']
    search_fields = ['command']
    readonly_fields = ['command']
    list_editable = ['is_run']
    class Meta:
        model = Rule

admin.site.register(Chain, ChainAdmin)
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Rule, RuleAdmin)

