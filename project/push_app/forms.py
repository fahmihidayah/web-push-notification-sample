from django.forms import Form, CharField, Textarea


class SendMessageForm(Form):

    title = CharField(max_length=200)

    message = CharField(max_length=255, widget=Textarea)