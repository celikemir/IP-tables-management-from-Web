# -*- coding: utf-8 -*-
from rest_framework import serializers

CHOICES = (
    ('start', 'start'),
    ('stop', 'stop')
)

class RuleSerializer(serializers.Serializer):
    rule_id = serializers.IntegerField(
        label='Rule ID',
    )

    action = serializers.ChoiceField(
        choices=CHOICES,
        label='action'
    )
