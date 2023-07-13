from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import  Text
from .forms import RegisterUserForm
from .hugging_request import query
from io import BytesIO
from elasticsearch import Elasticsearch
import matplotlib as plt, base64
from datetime import datetime



index_es = "notes"


def homepage(request):
    return render(request, "index.html")



# def new_text(request):
#     text = None
#     if request.method == 'POST':
#         text = request.POST.get('text', '')
#         output = query({
#             "inputs": text,
#         })
#         if type(output) == list:
#             emotion = output[0][0]["label"].capitalize()
#             new_text = Text(content=text, 
#                             emotion = emotion,
#                             patient_id = request.user)
#             new_text.save()
#             return render(request, 'add_text.html', {"emotion" : emotion})
#     return render(request, 'add_text.html')

def new_text(request):
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    if not request.user.is_authenticated: #if the user is not authenticated
        return HttpResponseRedirect(reverse("login")) #redirect to login page
    else:
        if request.method == 'POST':
            text = request.POST.get('text', '')
            output = query({
                "inputs": text,
            })
            emotion = output[0][0]["label"].capitalize()
            new_text = Text(content=text, 
                            emotion = emotion,
                            patient_id = request.user)
            new_text.save()

            # Ajouter à Elasticsearch
            es.index(index=index_es, doc_type='_doc', body={
                'patient_id': request.user.id,
                'patient_firstname': request.user.first_name,
                'patient_lastname': request.user.last_name,
                'emotion': emotion,
                'date': datetime.now().strftime('%Y-%m-%d'),  # Remplacer par la date appropriée
            })

            return render(request, 'add_text.html')
        return render(request, 'add_text.html')


def text_by_id(request, id):
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    
    query = {
        'query': {
            'term': {'patient_id': id}
        },
        'size': 1000
    }
    
    response = es.search(index=index_es, body=query)
    texts = []
    if 'hits' in response:
        hits = response['hits']['hits']
        texts = [hit['_source'] for hit in hits]

    
    context = {'all_texts': texts, "patient": User.objects.get(id=id)}
    return render(request, 'text_list.html', context)

# autres définitions de fonctions ...

def get_patient_texts(patient_id : int):
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    
    query = {
        'query': {
            'term': {'patient_id': patient_id}
        },
        'size': 1000
    }
    
    response = es.search(index=index_es, body=query)
    if 'hits' in response:
        hits = response['hits']['hits']
        texts = [hit['_source'] for hit in hits]
        return texts
    
    return []


def get_emotion_distribution(texts : list):
    emotion_distribution = {}
    
    for text in texts:
        emotion = text.get('emotion')
        if emotion:
            if emotion in emotion_distribution:
                emotion_distribution[emotion] += 1
            else:
                emotion_distribution[emotion] = 1
    print(emotion_distribution)
    return emotion_distribution


def pie_chart_view(emotion_distribution):
    plt.clf()
    # Generate the pie chart
    emotions = list(emotion_distribution.keys())
    counts = list(emotion_distribution.values())

    # Create the pie plot
    plt.pie(counts, labels=emotions, autopct='%1.1f%%')
    plt.axis('equal')

    # Convert the plot to an image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image as base64
    graphic = base64.b64encode(image_png).decode('utf-8')
    
    return graphic




def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('homepage')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register.html', {
        "form" : form,
        })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')

    else:
        return render(request, 'authentication/login.html') 

@login_required
def logout_user(request):
    logout(request)
    return redirect('homepage')