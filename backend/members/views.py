from rest_framework import viewsets
from members.models import Members
from members.serializers import MembersSerializer

class MembersViewSet(viewsets.ModelViewSet):
    serializer_class = MembersSerializer
    def get_queryset(self):
        return Members.objects.all()
