from rest_framework import serializers
from library import models as library_models
from datetime import timedelta
from django.db.models import Q
from django.core.exceptions import ValidationError

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'published_date', 'isbn']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = library_models.Table
        fields = ['table_number', 'capacity', 'location']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = library_models.Customer
        fields = ['full_name', 'phone_number']


class TableReservationSerializer(serializers.ModelSerializer):
    end_time = serializers.TimeField(required=False)
    customer_details = serializers.DictField(required=True)
    special_requests = serializers.CharField(required=False)

    class Meta:
        model = library_models.TableReservation
        fields = ['table', 'date', 'start_time', 'end_time', 'customer_details', 'number_of_guests', 
                  'special_requests']
        
    def create(self, validated_data):
        if not validated_data.get('end_time', None):
            end_time = validated_data.get('start_time') + timedelta(minutes=120)
            validated_data['end_time'] = end_time
        existing_overlap = library_models.TableReservation.objects.filter(Q(start_time__range=(validated_data['start_time'], validated_data['end_time'])) | Q(end_time__range=(validated_data['start_time'], validated_data['end_time']))).filter(date=validated_data['date'],
                                                                          table_id=validated_data['table_id'])
        if existing_overlap.exists():
            raise ValidationError("Time overlap with existing reservaltion")
        customer_details = validated_data.pop(customer_details)
        customer = library_models.Customer.objects.create(**customer_details)
        validated_data['customer_id'] = customer.id
        return super().create(validated_data)()
