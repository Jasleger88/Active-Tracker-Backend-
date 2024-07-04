from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Category
from .serializers.populated import PopulatedCategorySerializer
from .serializers.common import CategorySerializer


class CategoryListView(APIView):


    def get(self, _request):
        category = Category.objects.all()
        serialized_category = PopulatedCategorySerializer(category, many=True)
        return Response(serialized_category.data, status=status.HTTP_200_OK)
    
. 
    def post(self, request):
        category_to_add = CategorySerializer(data=request.data)
        try: 
            category_to_add.is_valid()
            category_to_add.save()
            return Response(category_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CategoryDetailView(APIView):
    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound(detail= "Cant find that Category")

    def get(self, request, pk):
        category = self.get_category(pk=pk)
        serialized_category = PopulatedCategorySerializer(category)
        return Response(serialized_category.data, status.HTTP_200_OK)


    def put(self, request, pk):
        category_to_update = self.get_category(pk=pk)
        update_category = CategorySerializer(category_to_update, data=request.data)

        if update_category.is_valid():
            updated_category.save()
            return Response(updated_category.data, status=status.HTTP_200_ACCEPTED)
        return Response(updated_category.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

