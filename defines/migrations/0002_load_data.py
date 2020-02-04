# -*- coding: utf-8 -*-
from django.db import migrations
from django.apps import apps

def load_data(apps, schema_editor):
    Chains = apps.get_model('defines.Chain')
    Chains.objects.create(chain_name='INPUT')
    Chains.objects.create(chain_name='FORWARD')
    Chains.objects.create(chain_name='OUTPUT')

    Protocols = apps.get_model('defines.Protocol')
    Protocols.objects.create(protocol_name='TCP')
    Protocols.objects.create(protocol_name='UDP')
    Protocols.objects.create(protocol_name='ICMP')

    Services = apps.get_model('defines.Service')
    Services.objects.create(service_name='http', service_port=80)
    Services.objects.create(service_name='https', service_port=443)
    Services.objects.create(service_name='ftp', service_port=21)
    Services.objects.create(service_name='smtp', service_port=25)
    Services.objects.create(service_name='smtp-ssl', service_port=587)
    Services.objects.create(service_name='ssh', service_port=22)


class Migration(migrations.Migration):
    dependencies = [
        ('defines', '0001_initial')
    ]
    operations = [
        migrations.RunPython(load_data)
    ]

#forma yuklenecek olan datalar