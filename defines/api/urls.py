from django.conf.urls import url

from defines.api.views import RuleAPIView

urlpatterns = [
    url(r'^rule-control/', RuleAPIView.as_view())
]
