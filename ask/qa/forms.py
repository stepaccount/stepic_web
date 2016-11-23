# -*- coding: utf-8 -*-

from django import forms
from .models import *

#Register form
class RegisterForm(forms.Form):
    username = forms.CharField(label = "User", max_length=50, required = True)
    email = forms.EmailField()
    password = forms.CharFiled(label = "Password", widget=forms.PasswordInput(), max_length = 50, required = True)
    def save(self):
        pass

#Login form
class LoginForm(forms.Form):
    username = forms.CharField(label = "User", max_length=50, required = True)
    password = forms.CharFiled(label = "Password", widget=forms.PasswordInput(), max_length = 50, required = True)
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
        que = Question(title = self.cleaned_data['title'], text = self.cleaned_data['text'])
        que.save()
        return que

#Answer addition form
class AnswerForm(forms.Form):
    text = forms.CharField(label = "Answer", widget = forms.Textarea)
    question = forms.IntegerField()
    hidden_id = forms.CharField(widget=forms.HiddenInput())
    def save(self):
        que_id = int(hidden_id)
        user_question = Question.objects.get(pk = que_id)
        user_answer = Answer(text = self.cleaned_data['text'], question = user_question)
        user_answer.save()
        return user_answer
