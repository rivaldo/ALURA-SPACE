from django.shortcuts import redirect, render
from usuarios.forms import LoginForms, CadastroForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

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
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        
        if form.is_valid():
            if form['senha'].value() != form['confirma_senha'].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('cadastro')
            
            nome = form['nome_login'].value()      
            email = form['email'].value()
            senha = form['senha'].value()   
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'usuario já existe.')
                return redirect(cadastro)
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!' )
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucessso!')
    return redirect('login')