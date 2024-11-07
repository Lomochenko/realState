from django import forms
from django_recaptcha.fields import ReCaptchaField

from Home.models import Advertising


class AdvertisingForm(forms.Form):
    captcha = ReCaptchaField()

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "نام و نام خانوادگی",
                                      "id": "name",
                                      }),

    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "شماره تلفن همراه",

                                      "type": "tel",
                                      "pattern": "[0]{1}[9]{1}[0-9]{9}",
                                      'oninvalid': "this.setCustomValidity('شماره وارد شده صحیح نمی باشد مثال "
                                                   ":09123456789 ')",
                                      'oninput': "setCustomValidity('')"}),

    )
    text = forms.CharField(
        strip=False,
        widget=forms.Textarea(attrs={"class": "form-control",
                                     "placeholder": "گذرواژه",
                                     "id": "message",
                                     "style": "height: 150px"
                                     }),
    )
