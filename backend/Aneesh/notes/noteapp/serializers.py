from rest_framework import serializers
from noteapp.models import Notes
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=('NoteId','NoteCont')


