from django import forms
from . import models, parser


class MyBookForm(forms.Form):
    MEDIA_CHOICES = (
        ('MYBOOK_RU', 'MYBOOK_RU'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'MYBOOK_RU':
            book_parser = parser.parser()
            for i in book_parser:
                models.MyBook.objects.create(**i)
