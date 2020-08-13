from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import SearchData


class SearchByLocationForm(ModelForm):
    class Meta:
        model = SearchData
        fields = ('search_location',)
        widgets = {
            'search_location': TextInput(attrs={'class': 'search-text', 'placeholder': 'Search Location'}),
        }


class DashboardSearchForm(ModelForm):
    class Meta:
        model = SearchData
        fields = ('search_location',)
        widgets = {
            'search_location': TextInput(attrs={'class': 'search-text-dashboard', 'placeholder': 'Search Location'}),
        }