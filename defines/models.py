# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from .validators import ip_validator

import os
# Create your models here.

class Chain(models.Model):
    chain_name = models.CharField(
        max_length=50
    )

    def __unicode__(self):
        return self.chain_name

    def __str__(self):
        return self.chain_name


class Protocol(models.Model):
    protocol_name = models.CharField(
        max_length=50
    )

    def __unicode__(self):
        return self.protocol_name

    def __str__(self):
        return self.protocol_name

class Service(models.Model):
    service_name = models.CharField(
        max_length=50,
    )
    service_port = models.IntegerField()

    def __unicode__(self):
        return "%s:%s" % (self.service_name, self.service_port)

    def __str__(self):
        return "%s:%s" % (self.service_name, self.service_port)

class Rule(models.Model):
    chain = models.ForeignKey(
        Chain,
        related_name='rule_chain',
    )

    protocol = models.ForeignKey(
        Protocol,
        related_name='rule_protocol',
    )

    source_port = models.IntegerField(
        null=True,
        blank=True,
    )
    destination_port = models.IntegerField(
        null=True,
        blank=True,
    )

    source_ip = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[ip_validator],
    )
    destination_ip = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[ip_validator],
    )

    operation = models.CharField(
        max_length=30,
    )

    command = models.TextField(
        null=True,
        blank=True,
    )

    is_run = models.BooleanField(
        default=False
    )

    timestamp = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )


    #form nesnelerinin kontrolü ile komutu üretiyoruz ve save ediyoruz.

    def save(self, *args, **kwargs):
        ignore_field_list = ['id', 'chain', 'protocol', 'operation', 'command', 'is_run']
        iptables_keywords = {
            'destination_port': '--dport',
            'source_port': '--sport',
            'source_ip': '-s',
            'destination_ip': '-d'
        }
        params = []
        for f in self._meta.fields:
            f = f.name
            if f in ignore_field_list:
                continue
            if iptables_keywords.get(f) and getattr(self, f):
                params.append("%s %s " % (iptables_keywords.get(f), getattr(self, f)))

        params = " ".join(params)
        command = "iptables -I %s -p %s %s -j %s" % (self.chain.chain_name, self.protocol.protocol_name.lower(), params, self.operation)
        self.command = command
        if settings.DEBUG:
            if self.is_run:
                print(self.command)
            else:
                print(self.command.replace("-I","-D"))
        else:
            if Rule.objects.filter(pk=self.pk).exists():
                if Rule.objects.get(pk=self.pk).is_run != self.is_run:
                    if self.is_run:
                        print("Command executed." + self.command)
                        os.system(self.command)
                    else:
                        print("Command deleted." + self.command.replace("-I", "-D"))
                        os.system(self.command.replace("-I","-D"))
        super(Rule, self).save(*args, **kwargs)


    def __unicode__(self):
        return "%s:%s" % (self.chain, self.protocol)

    def __str__(self):
        return "%s:%s" % (self.chain, self.protocol)
