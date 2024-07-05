from django.urls import path
from .views import LogListView, LogDetailView


# http://localhost:8000/shoe/
urlpatterns = [
    path('', LogListView.as_view()),
    path('<int:pk>/', LogDetailView.as_view()),
]

