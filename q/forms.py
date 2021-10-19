from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        labels = {
          'name': 'Nome',
          'email': 'Email',
          'body': 'Testo',
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'Campo richiesto!',}