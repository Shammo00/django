from django import forms
from .models import Topic ,Entry

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {
            'name': 'New Topic'
        }
class newEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {
            'text': 'New Entry'
        }
        widgets = {
            'text': forms.Textarea()
        }