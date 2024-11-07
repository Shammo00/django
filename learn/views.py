from django.shortcuts import render
from.models import Topic

# Create your views here.
def home (request):
    return render(request,'learn/index.html')
def topics (request):
    topic = Topic.objects.all()
    context = {
        "topics": topic
    }
    return render(request,'learn/topic.html',context)