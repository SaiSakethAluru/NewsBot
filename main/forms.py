from django import forms


class NewsFilterForm(forms.Form):
    countries = [(None, 'All'), ('in', 'India'), ('ru', 'Russia'), ('us', 'US')]
    categories = [(None, 'All'), ('business', 'Business'), ('entertainment', 'Entertainment'),
                  ('general', 'General')]

    country_dropdown = forms.CharField(label='Country', required=False, widget=forms.Select(choices=countries))
    category_dropdown = forms.CharField(label='Category', required=False, widget=forms.Select(choices=categories))

    def clean(self):
        super().clean()
