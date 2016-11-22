from django import forms

#Question addition form
class AskForm(forms.Form):
    title = forms.CharField(label = "Title")
    text = forms.CharField(label = "Question", widget = forms.Textarea)
    
#Answer addition form
class AnswerForm(forms.Form):
    text = forms.CharField(label = "Answer", widget = forms.Textarea)
    question = forms.CharField(widget = forms.Textarea)
    

    