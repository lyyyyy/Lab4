from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from lib_manage.views import hello,current_datetime,current_datetime2,addBook,addAuthor,Search,details,delete,update,main
from django.conf.urls.static import static  
from django.conf import settings  
  
#333
# Uncomment the next two lines to enable the admin:
<<<<<<< HEAD

=======

>>>>>>> C4

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^current_datetime/$',current_datetime),
    (r'^current_datetime2/$',current_datetime2),
    (r'^addBook/$',addBook),
    (r'^addAuthor/$',addAuthor),
    (r'^search/$',Search),
    (r'^main/$',main),
    (r'^details/$',details),
    (r'^delete/$',delete),
    (r'^update/$',update),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATIC_ROOT,}),
	
    # Examples:
    # url(r'^$', 'Lab_3.views.home', name='home'),
    # url(r'^Lab_3/', include('Lab_3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
