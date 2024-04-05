from django.shortcuts import redirect, render
from usuarios.forms import LoginForms, CadastroForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        
        if form.is_valid():
            if form['senha'].value() != form['cofirma_senha']:
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()      
            email = form['email'].value()
            senha = form['senha'].value()   
            
            if User.objects.filter(username=nome).exists():
                return redirect(cadastro)
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form':form})

