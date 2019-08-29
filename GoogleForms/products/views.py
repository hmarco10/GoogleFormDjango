from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect
)

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import ProductForm
from .models import Product
from .mixins import LoginRequiredMixin
from .forms import ProductForm


class ProductList(ListView):
    model = Product


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product


@login_required()
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    template = loader.get_template('new_product.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if action == 'signup':
            user = User.objects.create_user(username=username,
                                            password=password,
                                            last_name=last_name,
                                            first_name=first_name)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login/login.html', context)

#Funcion para Update para vistas basadas en funciones

def form_update(request, id_form):
        formulario = Product.objects.get(id=id_form)
        if request.method =='GET':
            form = ProductForm(instance=formulario)
        else:
            form= ProductForm(request.POST, instance=formulario)
            if form.is_valid():
                form.save()
            return redirect('/')
        return render(request,'new_product.html', {'form':form})


#funcion Delete para vistas basadas en funciones
def form_delete(request,id_form):
    formulario = Product.objects.get(id=id_form)
    if request.method =='POST':
        formulario.delete()
        return redirect('/')
    return render(request,'form_delete.html',{'formulario':formulario})









