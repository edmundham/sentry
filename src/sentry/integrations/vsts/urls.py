from __future__ import absolute_import, print_function

from django.conf.urls import patterns, url
from .webhooks import WorkItemWebhook, VstsSearchEndpoint
urlpatterns = patterns(
    '',
    url(r'^issue-updated/$', WorkItemWebhook.as_view(), name='sentry-extensions-vsts-issue-updated'),
    url(r'^search/(?P<organization_slug>[^\/]+)/(?P<integration_id>\d+)/$',
        VstsSearchEndpoint.as_view(),
        name='sentry-extensions-vsts-search'
        ),
)
