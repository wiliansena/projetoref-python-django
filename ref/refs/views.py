from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import refForm, colorForm
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Ref
from .models import Color

# Create your views here.

# Views das Referências:

@login_required
def refList(request):
    search = request.GET.get('search')
    
    if search:
        refs = Ref.objects.filter(reference__icontains=search)

    else:
        refs_list = Ref.objects.all().order_by('-created_at')
        #adicionando paginação na lista
        paginator = Paginator(refs_list, 3)
        page = request.GET.get('page')
    
        refs = paginator.get_page(page)
    return render(request, 'refs/list.html', {'refs': refs})


@login_required
def refView(request, id):
    ref = get_object_or_404(Ref, pk=id)
    return render(request, 'refs/ref.html', {'ref': ref})


@login_required
def newRef(request):
    if (request.method == 'POST'):
        form = refForm(request.POST)
        
        if form.is_valid():
            ref = form.save(commit=True)
            ref.save()
            return redirect('/')
    else:
        form = refForm()
        return render(request, 'refs/addref.html', {'form': form})


@login_required
def editRef(request, id):
    ref = get_object_or_404(Ref, pk=id)
    form = refForm(instance=ref)
    print(ref.reference)
    
    if (request.method == 'POST'):
        form = refForm(request.POST, instance=ref)

        if (form.is_valid()):
            ref.save()
            return redirect('/')
        else:
            return render(request, 'refs/editref.html', {'form': form, 'ref': ref})
    else:
        return render(request, 'refs/editref.html', {'form': form, 'ref': ref})


@login_required
def deleteRef(request, id):
    ref = get_object_or_404(Ref, pk=id)
    ref.delete()

    messages.info(request, 'Referência deletada com sucesso!')


    return redirect('/')

#Views da Cores:


@login_required
def colorList(request):

    search = request.GET.get('search')
    
    if search:
        colors = Color.objects.filter(color_text__icontains=search)

    else:
        colors_list = Color.objects.all()
        paginator = Paginator(colors_list, 3)
        page = request.GET.get('page')
        colors = paginator.get_page(page)

    return render(request, 'colors/list.html', {'colors': colors})



@login_required
def newColor(request):
    if (request.method == 'POST'):
        form = colorForm(request.POST)
        
        if form.is_valid():
            color = form.save(commit=True)
            color.save()
            return redirect('/')
    else:
        form = colorForm()
        return render(request, 'colors/addcolor.html', {'form': form})


@login_required
def editColor(request, id):
    color = get_object_or_404(Color, pk=id)
    form = colorForm(instance=color)
    print(color.color_text)
    
    if (request.method == 'POST'):
        form = colorForm(request.POST, instance=color)

        if (form.is_valid()):
            color.save()
            return redirect('colors/')
        else:
            return render(request, 'colors/editcolor.html', {'form': form, 'color': color})
    else:
        return render(request, 'colors/editcolor.html', {'form': form, 'color': color})



@login_required
def deleteColor(request, id):
    color = get_object_or_404(Color, pk=id)
    color.delete()

    messages.info(request, 'Cor deletada com sucesso!')
    return redirect('/')