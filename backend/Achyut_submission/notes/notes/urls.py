from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notesApp import views

urlpatterns = [
    path('', views.NotesList.as_view()),
    path('notes/<int:pk>/', views.NotesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)