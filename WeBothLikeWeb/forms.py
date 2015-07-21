from django import forms
from WeBothLikeCore.models import Question


class AnswerQuestionForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    answer = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((0, 'False'), (1, 'True')),
        widget=forms.RadioSelect
    )


class QuestionsResetForm(forms.Form):
    reset = forms.BooleanField()