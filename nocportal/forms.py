from django import forms
from django.forms import ModelForm

from nocportal.models import NocComment


class CommentForm(ModelForm):
    class Meta:
        model = NocComment
        fields = ['content', 'user', 'site']
        widgets = {
            'site': forms.HiddenInput()
        }

    # content_type = forms.CharField(widget=forms.HiddenInput)
    # object_id = forms.IntegerField(widget=forms.HiddenInput)
    # # parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    # content = forms.CharField(widget=forms.Textarea)