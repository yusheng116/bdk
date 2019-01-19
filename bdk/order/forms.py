from django import forms
from order.models import Order
from random import choice


class OrderForm(forms.ModelForm):
    name1=forms.CharField(
    label="姓氏",
    widget=forms.TextInput()
    )
    name2=forms.CharField(
    label="名字",
    widget=forms.TextInput()
    )
    country=forms.ChoiceField(  
    choices=(('台灣','台灣'),('香港','香港'),('澳門','澳門')),  
    label="國家/地區",
    widget=forms.Select()
    )
    PT=forms.CharField(
    label="郵遞區號",
    widget=forms.TextInput()
    )
    ADR=forms.CharField(
    label="地址",
    widget=forms.TextInput()
    )
    phone=forms.CharField(
    label="電話",
    widget=forms.TextInput()
    )
    number=forms.CharField(
    label="身份證字號",
    widget=forms.TextInput()
    )
    email=forms.CharField(
    label="電子郵件",
    widget=forms.TextInput()
    )
    shoes=forms.ChoiceField(  
        choices=(('New Balance MHANZSM1NT','New Balance MHANZSM1NT'),
                 ('ThreadborneFortis 3RC 2NT','ThreadborneFortis 3RC 2NT'),
                 ('NikeLeBron 16NT1','NikeLeBron 16NT1'),
                 ('AdidasHARDEN VOL. 3','AdidasHARDEN VOL. 3'),
                 ('Converse One Star MC18','Converse One Star MC18'),
                 ('VansChima Pro 2','VansChima Pro 2')),  
        label="鞋子種類",
        widget=forms.Select()
    )
    SD=forms.fields.ChoiceField(
        choices=(('標準','標準'),
                 ('快遞','快遞')),
        label='選擇寄送方式',
        widget=forms.widgets.RadioSelect
    )

    class Meta:
        model = Order
        fields = ['name1','name2','country','PT','ADR','phone','number','email','shoes','SD']
        
        
        
        
        
        
        
        