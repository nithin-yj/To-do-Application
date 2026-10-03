from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','description']


class EditForm(TodoForm):
    class Meta(TodoForm.Meta):
        fields=['title','description','status']
