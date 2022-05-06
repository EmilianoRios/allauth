from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-control',
            'maxlength':'16',
            'minlength':'3',
            'placeholder':'Usuario',
            'aria-label':'Username',
            'aria-describedby':'basic-addon1'
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-control',
            'placeholder':'Correo',
            'aria-label':'Email',
            'aria-describedby':'basic-addon1'
        })        
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-control',
            'maxlength':'16',
            'minlength':'3',
            'placeholder':'Contraseña',
            'aria-label':'Password1',
            'aria-describedby':'basic-addon1'
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-control',
            'maxlength':'16',
            'minlength':'3',
            'placeholder':'Confirmar Contraseña',
            'aria-label':'Password2',
            'aria-describedby':'basic-addon1'
        })                

    class Meta:
        model = User
        fields = ['username','email','password1','password2']