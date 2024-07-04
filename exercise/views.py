from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Exercise
from .serializers.populated import PopulatedExerciseSerializer
from .serializers.common import ExerciseSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class ExerciseListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get(self, _request):
        exercise = Exercise.objects.all()
        serialized_exercise = ExerciseSerializer(exercise, many=True)
        return Response(serialized_exercise.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        exercise_to_add = ExerciseSerializer(data=request.data)
        try: 
            exercise_to_add.is_valid()
            exercise_to_add.save()
            return Response(exercise_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ExerciseDetailView(APIView):
    def get_exercise(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            raise NotFound(detail="Can't Find that Exercise")


    def get(self, _request, pk):
        try:
            exercise = self.get_exercise(pk=pk)
            serialized_exercise = PopulatedExerciseSerializer(exercise)
            return Response(serialized_exercise.data, status=status.HTTP_200_OK)
        except Exercise.DoesNotExist:
            raise NotFound("Can't Find that Exercise")
    

    def put(self, request, pk):
        exercise_to_update = self.get_exercise(pk=pk)

        request.data['owner']= request.user.id

        if exercise_to_update.owner.id != request.user.id and not (request.user.is_staff or request.user.is_superuser):
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.data['owner'] = original_owner
       
        original_owner = exercise_to_update.owner.id

        updated_exercise = ExerciseSerializer(exercise_to_update, data=request.data)

        if updated_exercise.is_valid():
            updated_exercise.save()
            return Response(updated_exercise.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(updated_exercise.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):

        exercise_to_delete = self.get_exercise(pk=pk)

        if exercise_to_delete.owner != request.user.id and not (request.user.is_staff or request.user.is_superuser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        exercise_to_delete.delete()
        return Response(status=status.HTTP_200_NO_CONTENT)





