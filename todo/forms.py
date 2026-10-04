from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','description']
        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'cursive-input'
                }
            
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'cursive-input'
                }
            )
        }


class EditForm(TodoForm):
    class Meta(TodoForm.Meta):
        fields=['title','description','status']
        # widgets={
        #     **TodoForm.Meta.widgets,
        #     'status':forms.Select(
        #         attrs={
        #             'class':'cursive-input'
        #         }
        #     )
            
        # }
