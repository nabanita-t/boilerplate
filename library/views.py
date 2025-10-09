from rest_framework import viewsets, status, filters
from library import models as library_models
from library import serializers as library_serializer
from rest_framework.response import Response
from datetime import timedelta
from rest_framework.permissions import IsAuthenticated, AllowAny


# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "AUTH_HEADER_TYPES": ("Bearer",),
# }

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all().order_by('-id')
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#             """
#             create books
#             """
#             try:
#                 serializer = self.serializer_class(data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
#     def retrieve(self, request, pk=None, *args, **kwargs):
#             """
#             get books
#             """
#             try:
#                 book = self.get_object()
#                 serializer = self.serializer_class(book)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
#     def list(self, request, *args, **kwargs):
#             """
#             get all books
#             """
#             try:
#                 book = self.get_queryset()
#                 serializer = self.serializer_class(book, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
#     def update(self, request, pk=None, *args, **kwargs):
#             """
#             put books
#             """
#             try:
#                 book = self.get_object()
#                 serializer = self.serializer_class(book, data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
#     def partial_update(self, request, pk=None, *args, **kwargs):
#             """
#             patch books
#             """
#             try:
#                 book = self.get_object()
#                 serializer = self.serializer_class(book, data=request.data, partial=True)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
#     def destroy(self, request, pk=None, *args, **kwargs):
#             """
#             delete books
#             """
#             try:
#                 book = self.get_object()
#                 book.delete()
#                 return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            

class TableAPIView(viewsets.ModelViewSet):
    queryset = library_models.Table.objects.all().order_by('-table_number')
    serializer_class = library_serializer.TableSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['capacity', 'location']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
            """
            create table data
            """
            try:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    def retrieve(self, request, pk=None, *args, **kwargs):
            """
            get table deatils
            """
            try:
                table = self.get_object()
                serializer = self.serializer_class(table)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    def list(self, request, *args, **kwargs):
            """
            get all table list
            """
            try:
                table_objs = self.get_queryset()
                capacity = self.request.query_params.get("capacity", None)
                location = self.request.query_params.get("location", None)
                if capacity:
                     table_objs = table_objs.filter(capacity__gte=int(capacity))
                if location:
                     table_objs = table_objs.filter(location=str(location))
                serializer = self.serializer_class(table_objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    # def update(self, request, pk=None, *args, **kwargs):
    #         """
    #         put books
    #         """
    #         try:
    #             book = self.get_object()
    #             serializer = self.serializer_class(book, data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except Exception as e:
    #             return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    def partial_update(self, request, pk=None, *args, **kwargs):
            """
            patch books
            """
            try:
                table = self.get_object()
                serializer = self.serializer_class(table, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    def destroy(self, request, pk=None, *args, **kwargs):
            """
            delete books
            """
            try:
                table = self.get_object()
                table.delete()
                return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            

class TableReservationAPIView(viewsets.ModelViewSet):
    queryset = library_models.TableReservation.objects.all()
    serializer_class = library_serializer.TableReservationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
            """
            create table reservation data
            """
            try:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)