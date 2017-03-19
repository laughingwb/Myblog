from django.shortcuts import render
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Aricletype,Lifenote
from aboutme.models import Myself

# Create your views here.


@login_required()
def lifemanage(request):
    aricletype =  Aricletype.objects.all();
    return render(request, 'man/lifemanage.html',{'typeList':aricletype})

@login_required()
def addtype(request):
    typename = request.POST.get('aricletype', '')
    print(typename)
    aricletype = Aricletype.objects.create(type_name=typename)
    aricletype.save()
    typeAll = Aricletype.objects.all();
    return render(request, 'man/lifemanage.html', {'typeList': typeAll})

@login_required()
def addAricle(request):
    aricle_title = request.POST.get('title', '')
    aricle_type = request.POST.get('type', '')
    print(aricle_type)
    aricle_content = request.POST.get('content', '')
    typeAll = Aricletype.objects.all();
    typeObj = Aricletype.objects.filter(type_name=aricle_type)
    life_note = Lifenote.objects.create(aricletype=typeObj[0],title_note=aricle_title)
    life_note.content = aricle_content
    life_note.save();
    return render(request, 'man/lifemanage.html', {'typeList': typeAll})

@login_required()
def subtracttype(request):
    check_box_list = request.POST.getlist('check_box_list')
    print(check_box_list)
    if len(check_box_list) == 0:
        aricletype = Aricletype.objects.all();
        return render(request, 'man/lifemanage.html', {'typeList': aricletype})
    for type_name in check_box_list:
        aricletype = Aricletype.objects.filter(type_name=type_name)
        aricletype.delete();
    aricletype = Aricletype.objects.all();
    return render(request, 'man/lifemanage.html', {'typeList': aricletype})

@login_required()
def aricledetail(request):
    aricle_id = request.GET.get('aricle_id', '')
    print(aricle_id)
    aricledetail = Lifenote.objects.get(pk=aricle_id)
    myself = Myself.objects.all();
    return render(request, 'aricledetail.html',{'aricledetail':aricledetail,'myselfInfo':myself[0]})


def showHome(request):
    notelist = Lifenote.objects.all();
    myself = Myself.objects.all();
    return render(request, 'home.html',{'notelist':notelist,'myselfInfo':myself[0]})

def lifelist(request):
    return render(request, 'lifelist.html')
