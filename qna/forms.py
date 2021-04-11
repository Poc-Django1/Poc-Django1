from django import forms

from qna.models import Questionanswers


class QnaForm(forms.ModelForm):
    class Meta:
        model = Questionanswers
        fields = "__all__"

