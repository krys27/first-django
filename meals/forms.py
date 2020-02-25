from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class WriteReviewForm(forms.Form):
    review = forms.SlugField(help_text = 'Enter your review here')
    
    def clean_review(self):
        data = self.cleaned_data['review']

        # Check that the comment is longer than one word
        if len(data.split()) <=1:
            raise ValidationError(_('Please write a longer comment'))
        return data
