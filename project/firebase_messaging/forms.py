from django.forms import Form, CharField


class SendMessageForm(Form):

    title = CharField(max_length=255)

    message = CharField(max_length=255)

    user_id = CharField(max_length=100)