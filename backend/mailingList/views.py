# from django.shortcuts import render

from rest_framework import viewsets
from mailingList.models import MailingList
from mailingList.serializers import MailingListSerializer

class MailingListViewSet(viewsets.ModelViewSet):
    serializer_class = MailingListSerializer

    def get_queryset(self):
        return MailingList.objects.all()