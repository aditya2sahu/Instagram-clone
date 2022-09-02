from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form


class Usercreation(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            "class":"username",
            "unique":True,
            "placeholder":"Enter Your User Name",
            })
        self.fields['email'].widget.attrs.update({
            "class":"usereamil",
            "placeholder":"Enter Your Email Address",
            })
        self.fields['password1'].widget.attrs.update({
            "class":"userpass1",
            "placeholder":"Enter Your Password",
            })
        self.fields['password2'].widget.attrs.update({
            "class":"userpass1",
            "placeholder":"Confirm Your Password",
            })
    class Meta:
        model=User
        fields=['username','email','password1','password2']










