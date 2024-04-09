from django import forms

class LoginForms (forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Ex.: Rivaldo da Silva'
            }
        )
    )
    
    senha = forms.CharField(
        label= 'Digite sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
    
class CadastroForm ( forms.Form):
    nome_login = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TimeInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Ex.: Rivaldo da Silva'
            }
        )
    )
    
    email = forms.EmailField(
        label='Endereço de e-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: alguem@algumacoisa.com'
            }            
            
        )
    )
    senha = forms.CharField(
        label= 'Digite sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
    confirma_senha = forms.CharField(
        label= 'Confirme a sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder':'Digite sua senha novamente'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_login')        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            
 