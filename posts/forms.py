from django import forms
#from tinymce import TinyMCE
from .models import Post, Comment

'''
class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
'''
'''
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
        }))
    class Meta:
        model = Comment
        fields = ('content',)
'''

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'required':'true','class':"form-control", 'placeholder':"Name"}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':"Type your comment"}))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Name"}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':"Email"}),
            }