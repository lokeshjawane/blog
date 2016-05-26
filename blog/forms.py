from django import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import Blog

class Blogeditor(forms.Form):
    blog = forms.CharField(widget=CKEditorWidget())

