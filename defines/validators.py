#-*- coding:utf-8 -*-
from django.core.exceptions import ValidationError

import re


def ip_validator(value):
    ip_pattern = re.compile(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
    if value:
        if ip_pattern.match(value):
            return value
        else:
            raise ValidationError("Wrong IP.")
    return value
