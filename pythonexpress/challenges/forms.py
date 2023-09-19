from django import forms
from .models import Participant  # Import the Participant model if not already imported

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['code_solution']

    code_solution = forms.CharField(
        label='Your Code Solution',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'style': 'font-family: monospace;', }),
        help_text='Write your Python code solution here.'
    )
