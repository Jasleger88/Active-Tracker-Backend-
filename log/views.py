from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Log
from .serializers.common import LogSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers.populated import PopulatedLogSerializer


class LogListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        log = Log.objects.filter(owner = request.user.id)
        serialized_log = LogSerializer(log, many=True)
        return Response(serialized_log.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data["owner"]= request.user.id
        print("REQUEST DATA", request.data)
        log_to_add = LogSerializer(data=request.data)
        try: 
            log_to_add.is_valid()
            log_to_add.save()
            return Response(log_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LogDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    def get_log(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise NotFound(detail="Can't find that Log")

    def get(self, request, pk):
        try:
            log = self.get_log(pk=pk)
            serialized_log = PopulatedLogSerializer(log)
            return Response(serialized_log.data, status=status.HTTP_200_OK)
        except Log.DoesNotExist:
            return Response({"detail": "Can't find that Log"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        log_to_update = self.get_log(pk=pk)


        if log_to_update.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        original_owner = log_to_update.owner.id  
        request.data['owner'] = original_owner
            
        update_log = LogSerializer(log_to_update, data=request.data)

        if update_log.is_valid():
            update_log.save()
            return Response(update_log.data, status=status.HTTP_200_OK)
        return Response(update_log.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        log_to_delete = self.get_log(pk=pk)
        
        if log_to_delete.owner != request.user:
            raise PermissionDenied()

        log_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)