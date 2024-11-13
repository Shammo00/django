from django import forms
from .models import Topic ,Entry

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name','image']
        labels = {
            'name': 'New Topic',
            'image': 'Attach Image',
        }
class newEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text','image']
        labels = {
            'text': 'New Entry',
            'image': 'Attach Image',
        }
        widgets = {
            'text': forms.Textarea()
        }