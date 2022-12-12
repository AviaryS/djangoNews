from django import forms


class AddNews(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput)
    content = forms.CharField(label='Контент', widget=forms.Textarea)
    isPublish = forms.BooleanField(label='Опубликовать', initial=True)
    date = forms.DateField(label='Дата публикации')