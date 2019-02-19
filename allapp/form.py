from django import forms
from django.forms import ModelForm
from allapp.models import CvSend
from django.utils.translation import ugettext_lazy as _

class CvSendForm(forms.ModelForm):
	name=forms.CharField(label=_('Ad'))
	surname=forms.CharField(label=_('Soyad'))
	cv=forms.FileField(label=_('Cv'),widget=forms.FileInput(attrs={
        'class':'form-control-form-input',
        }
    ))

	cover_letter=forms.FileField(label=_('Tövsiyyə Məktubu'),widget=forms.FileInput(attrs={
        'class':'form-control-form-input',
        }
    ))
	class Meta:
		model=CvSend
		fields=[
			'name',
			'surname',
			'email',
			'cv',
			'cover_letter',

			]
		labels={
		'name':_('Ad'),
		'surname':_('Soyad'),
		'cover_letter':_('Tövsiyyə Məktubu')
		}