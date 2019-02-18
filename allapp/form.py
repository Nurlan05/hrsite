from django import forms
from django.forms import ModelForm
from allapp.models import CvSend


class CvSendForm(forms.ModelForm):

	class Meta:
		model=CvSend
		fields=[
			'name',
			'surname',
			'email',
			'cv',
			'cover_letter',

			]