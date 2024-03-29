from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList

from .models import Contact


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">{}</div>'.format(''.join([f'<p class="small error">{e}</p>' for e in self]))


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }
