from django.conf.urls import url
from rest_framework.fields import URLField
from noteapp import views


urlpatterns={
    url(r'^note$',views.noteapi),
    url(r'^note/([0-9]+)$',views.noteapi)
}