from django.shortcuts import render, redirect
from estoqueapp.forms import ItensForm
from estoqueapp.models import Itens

# Create your views here.
def home(request):
    dados = {}
    dados['db'] = Itens.objects.all()
    return render(request, 'index.html', dados)

def form(request):
    dados={}
    dados['form'] = ItensForm()
    return render(request, 'form.html', dados)

def create(request):
    form= ItensForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')