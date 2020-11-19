from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'takuhaikenpin', 'sonotakenpin', 'sex', 'memo')
        widgets = {
                    #'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'name': forms.Select(),
                    'takuhaikenpin': forms.NumberInput(attrs={'min':0}),
                    'sonotakenpin': forms.NumberInput(attrs={'min': 0}),

                    #'sex': forms.RadioSelect(), ←ラジオボタン
                    'sex': forms.Select(),  # プルダウンセレクト
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
