from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^about',views.about,name='about'),
    url(r'^donate',views.donate,name='donate'),
    url(r'^join',views.join,name='join'),
    url(r'^faq',views.faq,name='faq'),
    url(r'^feedback',views.feedback,name='feedback'),
    url(r'^contact',views.contact,name='contact'),
]