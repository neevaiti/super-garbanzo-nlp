from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
from .hugging_request import query


def new_text(request):
    text=None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        output = query({
            "inputs": text,
        })
        if not type(output) == dict:
            emotion = output[0][0]["label"].capitalize()
            new_text = Text(content=text, 
                            emotion = emotion)
            new_text.save()

            all_texts = Text.objects.all()
            return render(request, 'index.html', {"all_texts" : all_texts, "emotion" : emotion, "output": type(output)})
    return render(request, 'index.html')



# def new_text_by_id(request, id):
#     text=None
#     if request.method == 'POST':
#         text = request.POST.get('text', '')
#         output = query({
#             "inputs": text,
#         })
#         if not type(output) == dict:
#             emotion = output[0][0]["label"].capitalize()
#             new_text = Text(content=text, 
#                             emotion = emotion,
#                             patient_id = id)
#             new_text.save()

#             all_texts = Text.objects.filter(patient_id = patient_id)
#             return render(request, 'index.html', {"all_texts" : all_texts, "emotion" : emotion, "output": type(output)})
#     return render(request, 'index.html')