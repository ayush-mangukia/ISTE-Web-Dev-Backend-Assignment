from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from noteapp.models import Notes
from noteapp.serializers import NoteSerializer
# Create your views here.

@csrf_exempt
def noteapi(request,id=0):
    if(request.method == 'GET'):
        notes= Notes.objects.all()
        notes_serializer=NoteSerializer(notes,many=True)
        return JsonResponse(notes_serializer.data,safe=False)
    elif request.method == 'POST':
        note_data =JSONParser().parse(request)
        notes_serializer =NoteSerializer(data=note_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse('added successfully',safe=False)
        return JsonResponse('failed to add',safe=False)
    elif request.method == 'DELETE':
        note = Notes.objects.get(NoteId=id)
        note.delete()
        return JsonResponse('deleted',safe=False)


        

 