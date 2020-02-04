# -*- coding: utf-8 -*-
from django import forms
from django.apps import apps
from django.core.exceptions import ValidationError

from .validators import ip_validator

import re

Chain = apps.get_model('defines.Chain')
Protocol = apps.get_model('defines.Protocol')
Service = apps.get_model('defines.Service')


OPERATIONS = (
    ('ACCEPT', 'ACCEPT'),
    ('REJECT', 'REJECT'),
    ('DROP', 'DROP'),
)

class RuleForm(forms.Form):
    chain = forms.ModelChoiceField(queryset=Chain.objects.all(),
                                   empty_label=None,
                                   required=True,
                                   widget=forms.Select(
                                       attrs={'class': 'form-control'}
                                   ))

    protocol = forms.ModelChoiceField(queryset=Protocol.objects.all(),
                                      empty_label=None,
                                      required=True,
                                      widget=forms.Select(
                                          attrs={'class': 'form-control'}
                                      ))

    destination_port = forms.IntegerField(required=False,
                                          widget=forms.TextInput(
                                              attrs={'class': 'form-control hidden-object',
                                                     'placeholder': 'Destination Port'}
                                          ))

    source_port = forms.IntegerField(required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control hidden-object',
                                                'placeholder': 'Source Port'}
                                     ))

    destination_ip = forms.CharField(required=False,
                                     validators=[ip_validator],
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control hidden-object',
                                                'placeholder': 'Destination IP'}
                                     ))

    source_ip = forms.CharField(required=False,
                                validators=[ip_validator],
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control hidden-object',
                                           'placeholder': 'Source IP'}
                                ))

    operation = forms.CharField(required=True,
                                widget=forms.Select(
                                    attrs={'class': 'form-control'},
                                    choices=OPERATIONS,
                                ))


class ServicesForm(forms.Form):
    source_service = forms.ModelChoiceField(queryset=Service.objects.all(),
                                            required=False,
                                            empty_label='Source Services',
                                            widget=forms.Select(
                                                attrs={'class': 'form-control'}
                                            ))
    destination_service = forms.ModelChoiceField(queryset=Service.objects.all(),
                                                 required=False,
                                                 empty_label='Destination Services',
                                                 widget=forms.Select(
                                                     attrs={'class': 'form-control'}
                                                 ))

