from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteModel,EmpresaModel, LoginModel
from .forms import ClienteForm,EmpresaForm, LoginForm
from . import views
from django.contrib.auth.hashers import check_password
from .utils import validar

# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)       
        if ClienteModel.objects.filter(cpf=form.data['cpf']).exists():
            messages.error(request,'Este cliente já foi cadastrado!') 
        elif len(form.data['cpf']) != 11:
             messages.error(request,'O CPF informado é inválido!') 
        else:
            cliente = ClienteModel()
            cliente.cpf = form.data['cpf']
            cliente.nome = form.data['nome']
            cliente.telefone = form.data['telefone']
            cliente.endereco = form.data['endereco']
            cliente.email = form.data['email']
            cliente.senha = form.data['senha']
            cliente.save()
                      
    return render(request, 'cadastro.html')


def empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)       
        if EmpresaModel.objects.filter(cnpj=form.data['cnpj']).exists():
            messages.error(request,'Esta empresa já foi cadastrado!') 
        elif len(form.data['cnpj']) != 14:
             messages.error(request,'O CNPJ informado é inválido!') 
        else:
            empresa = EmpresaModel()
            empresa.cnpj = form.data['cnpj']
            empresa.nome = form.data['nome']
            empresa.telefone = form.data['telefone']
            empresa.endereco = form.data['endereco']
            empresa.email = form.data['email']
            empresa.senha = form.data['senha']
            empresa.save()
            
    return render(request, 'empresa.html')


def login(request):
    
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        resultado_validacao = validar(cpf, senha)

        if resultado_validacao[0]:  # Verifica se a validação foi bem-sucedida
            validado, usuario = resultado_validacao
            return render(request, 'index.html', {'usuario': usuario})
    # Restante do seu código
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    # Trate o caso em que a validação não foi bem-sucedida
            return render(request, 'index.html', {'erro': 'Credenciais inválidas'})



    return render(request, 'login.html')

def pontos(request):
    return render(request, 'pontos.html')
    

    

def produto(request):
    return render(request, 'produto.html')

def coleta(request):
    empresas = EmpresaModel.objects.all()
    return render(request, 'coleta.html', {'empresas': empresas})
    

def ticket(request):
    return render(request, 'ticket.html')

def material(request):
    return render(request, 'material.html')