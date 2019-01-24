from rest_framework import serializers
from contactapp.models import Contact


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'email',)