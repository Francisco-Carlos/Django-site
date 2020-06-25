from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Livros
# Create your views here.

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    request(logout)
    return redirect('/login/')

@login_required(login_url='/login/')
def lista_all(request):
    livros = Livros.objects.filter(active=True)
    busca = request.GET.get('seacher')
    if busca:
        livros= Livros.objects.filter(Titulo=busca)
    return render(request,'lista.html', {'livros':livros})

def list_user(request):
    livros = Livros.objects.filter(active=True, User=request.user)
    return render(request,'lista.html',{'livros':livros})

def livro_detail(request,id):
    livros = Livros.objects.get(active=True,id=id)
    return render(request,'detalhes.html',{'livros':livros})

@login_required(login_url='/login/')
def livro_regis(request):
    livro_id= request.GET.get('id')
    if livro_id:
        livro= Livros.objects.get(id=livro_id)
        if livro.User==request.user:
            return render(request,'registro.html',{'livro':livro})
    return render(request,'registro.html')

@login_required(login_url='/login/')
def set_livro(request):
    tit = request.POST.get('titulo')
    cate = request.POST.get('categoria')
    ima = request.FILES.get('image')
    resu = request.POST.get('resumo')
    val = request.POST.get('valor')
    user = request.user
    livro_id = request.POST.get('livro_id')
    if livro_id:
        livro = Livros.objects.get(id=livro_id)
        if user == livro.User:
            livro.Titulo = tit
            livro.Categoria = cate
            livro.Valor = val
            livro.Resumo = resu
            if ima:
                livro.Image = ima
            livro.save()
    else:
        livro = Livros.objects.create(Titulo=tit,Categoria=cate,Image=ima,User=user,Valor=val,Resumo=resu)
    url = f'/livros/detail/{livro.id}/'
    return redirect(url)

def del_livro(request,id):
    livro = Livros.objects.get(id=id)
    if livro.User==request.user:
        livro.delete()
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'usuario e senha errado')
    return redirect('/login/')