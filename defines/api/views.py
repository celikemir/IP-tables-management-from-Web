# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from defines.models import Rule
from defines.api.serializers import RuleSerializer


class RuleAPIView(APIView):
    http_method_names = ['post']

    def post(self, request, format=None):
        serializer = RuleSerializer(data=request.data)
        if serializer.is_valid():
            rule = Rule.objects.filter(pk=serializer.validated_data['rule_id'])
            if rule.exists():
                rule = rule[0]
                if serializer.validated_data['action'] == "start":
                    rule.is_run = True
                else:
                    rule.is_run = False
                rule.save()
                return Response(data={'detail': 'OK'},status=status.HTTP_200_OK)
            else:
                raise ValidationError(detail="Rule is not found")
        else:
            raise Response(status=status.HTTP_404_NOT_FOUND)
