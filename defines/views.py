# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from .forms import *
from .models import Rule

import os
# Create your views here.

class AddRuleView(View):
    template_name = 'add_rule.html'
    context = {}
    rule_form = RuleForm
    service_form = ServicesForm

    def get(self, request):
        self.context['form'] = self.rule_form(request.POST or None)
        self.context['service_form'] = self.service_form(request.POST or None)

        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.rule_form(request.POST or None)
        if form.is_valid():
            chain = form.cleaned_data.pop('chain')
            protocol = form.cleaned_data.pop('protocol')
            operation = form.cleaned_data.pop('operation')
            Rule.objects.create(chain=chain,
                                protocol=protocol,
                                operation=operation,
                                **form.cleaned_data)

        self.context['form'] = form
        self.context['service_form'] = self.service_form(request.POST or None)
        return render(request, self.template_name, self.context)


class RuleListView(View):
    template_name = 'rule_list.html'
    context = {}

    def get(self, request):
        self.context['rules'] = Rule.objects.all().order_by('-is_run', '-timestamp', '-id')
        return render(request, self.template_name, self.context)

    def post(self, request):
        rid = request.POST.get('rule_id')
        rule = Rule.objects.filter(pk=rid)
        if rule.exists():
            rule = rule[0]
            rule.is_run = False
            rule.save()

            rule.delete()

        self.context['rules'] = Rule.objects.all().order_by('-is_run', '-timestamp', '-id')
        return render(request, self.template_name, self.context)
