from django import forms

from anime_app.models import Anime, AnimeMedia, Comments


class SearchForm(forms.Form):
    search = forms.CharField()


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'org_title', 'description', 'avatar', 'created_year', 'status']
        widgets = {
            'description': forms.Textarea()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


class AnimeMediaForm(forms.ModelForm):
    class Meta:
        model = AnimeMedia
        fields = ['anime', 'series', 'name_of_series', 'video']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']

        widgets = {'body': forms.Textarea()}
