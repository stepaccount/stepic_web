# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import *

#Register form
class RegisterForm(forms.Form):
    username = forms.CharField(label = "User", max_length=50, required = True)
    email = forms.EmailField()
    password = forms.CharField(label = "Password", widget=forms.PasswordInput(), max_length = 50, required = True)
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
            #No exception - user already exists
            raise forms.ValidationError(u'Пользователь с таким именем уже существует', code=9)
        except User.DoesNotExist:
            pass
        return username

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        user.save()
        return user

#Login form
class LoginForm(forms.Form):
    username = forms.CharField(label = "User", max_length=50, required = True)
    password = forms.CharField(label = "Password", widget=forms.PasswordInput(), max_length = 50, required = True)
    def save(self):
        pass

#Question addition form
class AskForm(forms.Form):
    title = forms.CharField(label = "Title")
    text = forms.CharField(label = "Question", widget = forms.Textarea)
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) == 0:
            raise forms.ValidationError(u'Заголовок вопроса не может быть пустым', code=10)
        return title
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) == 0:
            raise forms.ValidationError(u'Текст вопроса не может быть пустым', code=11)
        return text
        
    def save(self):
        #create new question
        #TODO с русскоязычным содержанием форм НЕ РАБОТАЕТ, бросает исключение!!!
        que = Question(title = self.cleaned_data['title'], text = self.cleaned_data['text'], author = self._user)
        que.save()
        return que

#Answer addition form
class AnswerForm(forms.Form):
    text = forms.CharField(label = "Answer", widget = forms.Textarea)
    question = forms.IntegerField()
    hidden_id = forms.CharField(widget=forms.HiddenInput())
    def save(self):
        que_id = int(self.cleaned_data['hidden_id'])
        user_question = Question.objects.get(pk = que_id)
        user_answer = Answer(text = self.cleaned_data['text'], question = user_question, author = self._user)
        user_answer.save()
        return user_answer
