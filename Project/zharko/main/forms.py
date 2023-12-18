from django import forms
from django.core.exceptions import ValidationError

class AddReview(forms.Form):

    author = forms.CharField(label="Имя", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class":"form-control"}))
    comment = forms.CharField(label="Отзыв", widget=forms.Textarea(attrs={"class":"form-control", "rows":"7"}))
    image = forms.ImageField(label = "Фото работы")

class Request(forms.Form):

    name = forms.CharField(label='Ваше имя', max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(label='Номер телефона', max_length=9, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Например: 291234567"}))

    # def clean_phone(self):
    #     try:
    #         self.cleaned_data['phone'] = int(self.cleaned_data['phone'])
    #         return self.cleaned_data['phone']
    #     except:
    #         raise ValidationError("Телефон должен содержать только цифры!")
