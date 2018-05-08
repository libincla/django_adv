"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from mysite.views import hi, current_datetime, hours_ahead, show_ua, display_meta, display_whole 
from books import views
from books.views import PublisherList, BookList


extra_patterns = [
    url(r'^mytest/$', views.mytest),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hi/$',  hi),
    url(r'^time/$', current_datetime),
    url(r'^other_time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^showua/$', show_ua),
    url(r'^dm/$', display_meta),
    url(r'^dw/$', display_whole),
    url(r'^search/$', views.search),
    url(r'^search-form/$', views.search_form),
    url(r'^contact/$', views.contact),
    url(r'^aha/', include(extra_patterns), {'testid': 9}),
    url(r'^publishers/$', PublisherList.as_view()),
    #url(r'^time/plus/\d{1,2}/$', hours_ahead)
]

