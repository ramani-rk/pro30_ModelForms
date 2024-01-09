from django import forms
from app.models import *

class TopicForm (forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebForm (forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'

class AccessForm (forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'