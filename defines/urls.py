from django.conf.urls import url

from defines.views import AddRuleView, RuleListView

urlpatterns = [
    url(r'^add-rule/', AddRuleView.as_view()),
    url(r'^rules/', RuleListView.as_view())
]
