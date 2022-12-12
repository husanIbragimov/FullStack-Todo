from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['priority'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['author']





