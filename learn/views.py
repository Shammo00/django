from django.shortcuts import render , redirect
from.models import Topic
from .forms import NewTopicForm


# Create your views here.
def home (request):
    return render(request,'learn/index.html')
def topics (request):
    topic = Topic.objects.all()
    context = {
        "topics": topic
    }
    return render(request,'learn/topics.html',context)

def topic (request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entry = topic.entry_set.order_by('-date_added')
    context = {
        "topic":topic,
        "entries":entry
    }
    return render(request,'learn/topic_detail.html',context)

def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learn:topics')
    else:
        form = NewTopicForm()
    context = {
        "form": form
    }
    return render(request, 'learn/new_topic.html', context)