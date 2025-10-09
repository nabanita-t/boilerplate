# from rest_framework.filters import BaseFilterBackend
# import django_filters
# from django.utils import timezone
# from django.db.models import Q

# from project.apps.common.constant import Constants
# from project.apps.user import models as user_models
# from django.utils.dateparse import parse_date


# class DisciplineFilter(BaseFilterBackend):
#     """Filter the discipline of the internal nurse"""
#     param = "discipline[]"

#     def filter_queryset(self, request, queryset, view):
#         disciplines = request.query_params.getlist(self.param, [])
#         if disciplines:
#             return queryset.filter(discipline_id__in=disciplines)
#         return queryset


# class DepartmentFilter(BaseFilterBackend):
#     """Filter the department of the internal nurse"""
#     param = "department[]"

#     def filter_queryset(self, request, queryset, view):
#         departments = request.query_params.getlist(self.param, [])
#         if departments:
#             return queryset.filter(department_id__in=departments)
#         return queryset


# class FacilityFilter(BaseFilterBackend):
#     """Filter the discipline of the internal nurse"""
#     param = "facility"

#     def filter_queryset(self, request, queryset, view):
#         facilities = request.query_params.getlist(self.param, [])
#         if facilities:
#             return queryset.filter(id__in=facilities)
#         return queryset
