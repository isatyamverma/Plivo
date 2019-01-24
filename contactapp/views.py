# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from contactapp.serializers import ContactSerializer
from core.resources import Paginator
from .models import Contact


class ContactView(APIView):

    queryset = Contact.objects.all()

    def get_object(self, pk):
        try:
            return Contact.objects.get(id=pk)
        except Contact.DoesNotExist:
            raise Http404

        return contact

    def __filter(self, queryset, query_params):
        email = query_params.get('email', '')
        name = query_params.get('name', '')
        contacts = queryset.filter(email__icontains=email, first_name__icontains=name)

        return contacts

    def get(self, request):
        page_number = request.query_params.get('page', -1)
        page_size = request.query_params.get('size', -1)

        contacts = self.__filter(self.queryset, request.query_params)
        paginator = Paginator(contacts, ContactSerializer, page_size=page_size, page_number=page_number)

        response = paginator.data
        return JsonResponse(response)

    def post(self, request, format=None):

        data = request.data
        contact_serializer = ContactSerializer(data)

        if contact_serializer.is_valid(raise_exception=True):
            contact_serializer.save()

        return JsonResponse(contact_serializer.data)

    def put(self, request, pk):
        data = request.data
        contact = self.get_object(pk)

        contact_serializer = ContactSerializer(contact, data)

        if contact_serializer.is_valid(raise_exception=True):
            contact_serializer.save()

        return JsonResponse(contact_serializer.data)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()

        return Response(status='204')