from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import Produtoform

# Create your views here.


@login_required()
def prod_list(request):
    prod = Produto.objects.all()
    return render(request, 'prod.html', {'prod': prod})


@login_required()
def prod_new(request):
    form = Produtoform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('prod_list')
    return render(request, 'prod_form.html', {'form': form})


@login_required()
def prod_update(request, id):
    prods = get_object_or_404(Produto, pk=id)
    form = Produtoform(request.POST or None, request.FILES or None, instance=prods)
    if form.is_valid():
        form.save()
        return redirect('prod_list')
    return render(request, 'prod_form.html', {'form': form})


@login_required()
def prod_delete(request, id):
    prods = get_object_or_404(Produto, pk=id)
    form = Produtoform(request.POST or None, request.FILES or None, instance=prods)
    if request.method == 'POST':
        prods.delete()
        return redirect('prod_list')

    return render(request, 'prod_delete_confirm.html', {'form': form})
