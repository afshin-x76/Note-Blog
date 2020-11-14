from django import forms
from .models import Post, Comment, Author
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "comment here"
    }))
    class Meta:
        model = Comment
        fields = ('comment',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_CommentForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'thumbnail', 'categories']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-PostForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['age', 'profile_picture']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-addauthorForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))

