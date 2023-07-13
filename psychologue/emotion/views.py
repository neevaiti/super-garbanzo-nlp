from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import  Text
from .forms import RegisterUserForm
from .hugging_request import query
from io import BytesIO
from elasticsearch import Elasticsearch
import matplotlib as plt, base64

index_name = "notes"

def homepage(request):
    return render(request, "index.html")



def new_text(request):
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
            return render(request, 'add_text.html')
        return render(request, 'add_text.html')

def text_by_id(request, id):
    # text=None
    # all_texts = Text.objects.filter(patient_id = id)
    # text = request.POST.get('text', '')
    # output = query({
    #     "inputs": text,
    # })
    # if not type(output) == dict:
    #     emotion = output[0][0]["label"].capitalize()
    #     new_text = Text(content=text, 
    #                     emotion = emotion,
    #                     patient_id = id)
    #     new_text.save()

    #     return render(request, 'index.html', {"all_texts" : all_texts, "emotion" : emotion, "output": type(output)})
    
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    
    query = {
        'query': {
            'term': {'Text.patient_id': id}
        },
        'size': 1000
    }
    
    response = es.search(index=index_name, body=query)
    if 'hits' in response:
        hits = response['hits']['hits']
        texts = [hit['_source'] for hit in hits]
        return texts
    
    return render(request, 'text_list.html', {"texts" : texts})




def get_patient_texts(patient_id : int):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    
    query = {
        'query': {
            'term': {'Text.patient_id': patient_id}
        },
        'size': 1000
    }
    
    response = es.search(index='textes', body=query)
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

def logout_user(request):
    logout(request)
    return redirect('homepage')