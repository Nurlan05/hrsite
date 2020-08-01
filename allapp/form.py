from django import forms
from django.forms import ModelForm
from allapp.models import CvSend
from django.utils.translation import ugettext_lazy as _

class CvSendForm(forms.ModelForm):
	name=forms.CharField(label=_('Ad'))
	cv=forms.FileField(label=_('Cv'),widget=forms.FileInput(attrs={
        'class':'form-control-form-input',
        }
    ))

	cover_letter=forms.FileField(required=False,label=_('Tövsiyyə Məktubu'),widget=forms.FileInput(attrs={
        'class':'form-control-form-input',
        }
    ))

	class Meta:
		model=CvSend
		fields=[
			'name',
			'email',
			'cv',
			'cover_letter',

			]
		labels={
		'name':_('Ad'),
		'cover_letter':_('Tövsiyyə Məktubu')
		}