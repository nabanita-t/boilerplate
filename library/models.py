# Create your models here.
import uuid

from django.db import models


class BaseManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class BaseModel(models.Model):
    """Base Model class to add a id, created_at and updated_at field as common for all models.
    properties: id (uuid), created_at, updated_at (timestamp)
    """

    class Meta:
        """Abstract base model class.
        abstract = True (abstract base class),
        ordering = ['field'],
        db_table = 'custom_db_table'
        Note: Django does make one adjustment to the Meta class of an abstract base class: before installing the Meta attribute, it sets abstract=False.
        """
        abstract = True

    objects = BaseManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(default=None, null=True, editable=False)

    def __str__(self):
        """print: {id}/created_date
        :return:
        """
        return '{}-{}'.format(self.id, self.created_at)


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Table(BaseModel):
    STATUS_CHOICES = (("INDOOR", "INDOOR"), 
                      ("OUTDOOR", "OUTDOOR"))
    table_number = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255, choices=STATUS_CHOICES, default="INDOOR")

    def __str__(self):
        return f"{self.table_number} - {self.capacity} - {self.location}"
    
class Customer(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"


class TableReservation(BaseModel):
    table = models.ForeignKey(Table, on_delete=models.RESTRICT, related_name='table_reservation')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_guests = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='table_customer')
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.table.table_number} - {self.date} - {self.start_time} - {self.end_time}"
    

# Table Name - Restaurant
# Fields - table number, capacity, location(indoor/outdoor)

# Table - TableReservation
# Fields - table (FK), date, start_time, end_time, number_of_guests, customer(FK), special_requests

# Customer Table
# Fields: full_name, phone_number


class UrlArchive(BaseModel):
    original_url = models.CharField(max_length=255, unique=True)
    shortened_url = models.CharField(max_length=8, unique=True)
    
    def __str__(self):
        return f"{self.original_url} - {self.shortened_url} "
