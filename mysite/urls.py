from django.conf.urls import include, url
from django.contrib import admin
from blog.views import hello_world,home,post_detail
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world, name='hello'),
    url(r'^$', home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
