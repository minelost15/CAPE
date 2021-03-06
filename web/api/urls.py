# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r"^$", views.index, name='api'),
    url(r"^tasks/create/file/$", views.tasks_create_file),
    url(r"^tasks/create/url/$", views.tasks_create_url),
    url(r"^tasks/create/vtdl/$", views.tasks_vtdl),
    url(r"^tasks/search/md5/(?P<md5>([a-fA-F\d]{32}))/$", views.tasks_search),
    url(r"^tasks/search/sha1/(?P<sha1>([a-fA-F\d]{40}))/$", views.tasks_search),
    url(r"^tasks/search/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", views.tasks_search),
    url(r"^tasks/extendedsearch/$", views.ext_tasks_search),
    url(r"^tasks/list/$", views.tasks_list),
    url(r"^tasks/list/(?P<limit>\d+)/$", views.tasks_list),
    url(r"^tasks/list/(?P<limit>\d+)/(?P<offset>\d+)/$", views.tasks_list),
    url(r"^tasks/list/(?P<limit>\d+)/(?P<offset>\d+)/(?P<window>\d+)/$", views.tasks_list),
    url(r"^tasks/view/(?P<task_id>\d+)/$", views.tasks_view),
    url(r"^tasks/reschedule/(?P<task_id>\d+)/$", views.tasks_reschedule),
    url(r"^tasks/delete/(?P<task_id>\d+)/$", views.tasks_delete),
    url(r"^tasks/status/(?P<task_id>\d+)/$", views.tasks_status),
    url(r"^tasks/get/report/(?P<task_id>\d+)/$", views.tasks_report),
    url(r"^tasks/get/report/(?P<task_id>\d+)/(?P<report_format>\w+)/$", views.tasks_report),
    url(r"^tasks/get/iocs/(?P<task_id>\d+)/$", views.tasks_iocs),
    url(r"^tasks/get/iocs/(?P<task_id>\d+)/(?P<detail>detailed)/$", views.tasks_iocs),
    url(r"^tasks/get/screenshot/(?P<task_id>\d+)/$", views.tasks_screenshot),
    url(r"^tasks/get/screenshot/(?P<task_id>\d+)/(?P<screenshot>\d{1,4})/$", views.tasks_screenshot),
    url(r"^tasks/get/procmemory/(?P<task_id>\d+)/$", views.tasks_procmemory),
    url(r"^tasks/get/procmemory/(?P<task_id>\d+)/(?P<pid>\d{1,5})/$", views.tasks_procmemory),
    url(r"^tasks/get/fullmemory/(?P<task_id>\d+)/$", views.tasks_fullmemory),
    url(r"^tasks/get/pcap/(?P<task_id>\d+)/$", views.tasks_pcap),
    url(r"^tasks/get/dropped/(?P<task_id>\d+)/$", views.tasks_dropped),
    url(r"^tasks/get/surifile/(?P<task_id>\d+)/$", views.tasks_surifile),
    url(r"^files/view/md5/(?P<md5>([a-fA-F\d]{32}))/$", views.files_view),
    url(r"^files/view/sha1/(?P<sha1>([a-fA-F\d]{40}))/$", views.files_view),
    url(r"^files/view/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", views.files_view),
    url(r"^files/view/id/(?P<sample_id>\d+)/$", views.files_view),
    url(r"^files/get/(?P<stype>md5)/(?P<value>([a-fA-F\d]{32}))/$", views.get_files),
    url(r"^files/get/(?P<stype>sha1)/(?P<value>([a-fA-F\d]{40}))/$", views.get_files),
    url(r"^files/get/(?P<stype>sha256)/(?P<value>([a-fA-F\d]{64}))/$", views.get_files),
    url(r"^files/get/(?P<stype>task)/(?P<value>\d+)/$", views.get_files),
    url(r"^machines/list/$", views.machines_list),
    url(r"^machines/view/(?P<name>[\w$-/:-?{-~!^_`\[\]]+)/$", views.machines_view),
    url(r"^cuckoo/status/$", views.cuckoo_status),
    url(r"^tasks/get/rollingsuri/(?P<window>\d+)/$", views.tasks_rollingsuri),  
    url(r"^tasks/get/rollingshrike/(?P<window>\d+)/$", views.tasks_rollingshrike),
    url(r"^tasks/get/rollingshrike/(?P<window>\d+)/(?P<msgfilter>[\w$-/:-?{-~!^_`\[\]\s\x5c]+)/$", views.tasks_rollingshrike) 
]
