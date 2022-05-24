from django import forms


class ChatForm(forms.Form):
    message_text = forms.CharField(label="Ваше сообщение:", widget=forms.TextInput)
