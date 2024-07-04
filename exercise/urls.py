from django.urls import path
from .views import ExerciseListView, ExerciseDetailView


# http://localhost:8000/exercise/
urlpatterns = [
    path('', ExerciseListView.as_view()),
    path('<int:pk>/', ExerciseDetailView.as_view()),
]