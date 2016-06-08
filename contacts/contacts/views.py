from django.shortcuts import get_object_or_404, render, render_to_response
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from contacts.forms import UploadImageForm, RegistrationForm, PostAdminForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            request.session['is_active'] = True
            # Redirect to a success page.
            # return HttpResponseRedirect("sdfghjkl;';")
            return HttpResponseRedirect('/contacts')
        else:
            # Show an error page
            # return HttpResponseRedirect("sfsdgsdgsggggggggggggg")
            return render(request, 'contacts/login.html')
    else:
        return render(request, 'contacts/login.html')


@login_required(login_url='/contacts/login')
def index(request):
    if 'is_active' in request.session:
        cntct = Contacts.objects.all()
        comm = Comments.objects.all()
        language = 'en-gb'
        if 'sessionid' in request.COOKIES:
            language = request.COOKIES['sessionid']
            response = HttpResponse("sdfsdf")
            response.set_cookie('lang', language)
        editor = PostAdminForm()
        output = {'cntct': cntct, 'comm': comm, 'language': language, 'editor': editor}
        return render(request, 'contacts/index.html', output)
    else:
        editor = PostAdminForm()
        return render(request, 'contacts/login.html', {'editor': editor})
        # return HttpResponse('sdfsdfsdfsdfjj')


def detail(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    return render(request, 'contacts/detail.html', {'contact': contact})


def new(request):
    img = UploadImageForm()
    return render(request, 'contacts/new.html', {'img': img})


def addcon(request):
    cntct = Contacts(fname=request.POST['fname'], mname=request.POST['mname'], lname=request.POST['lname'],
                     image=request.FILES['image'])
    cntct.save()
    return HttpResponseRedirect('/contacts')


def editcon(request, cont_id):
    contact = get_object_or_404(Contacts, pk=cont_id)
    img = UploadImageForm()
    return render(request, 'contacts/edit.html', {'contact': contact, 'img': img})


def updatecon(request):
    # ontact = Contacts.objects.filter(id=request.POST['id']).update(fname=request.POST['fname'], mname=request.POST['mname'], lname=request.POST['lname'], image = request.FILES['image'])
    # return render(request, 'contacts/edit.html', {'contact' : contact})
    cntct = Contacts(id=request.POST['id'], fname=request.POST['fname'], mname=request.POST['mname'],
                     lname=request.POST['lname'], image=request.FILES['image'])
    cntct.save()
    return HttpResponseRedirect('/contacts')


def deletecon(request, cont_id):
    Contacts.objects.get(pk=cont_id).delete()
    # return render(request, 'contacts/edit.html', {'contact' : contact})
    return HttpResponseRedirect('/contacts')


def addcomm(request, cont_id):
    comm = Comments(f_name_id=cont_id, comment=request.POST['comment'])
    comm.save()
    return HttpResponseRedirect('/contacts')


def login(request):
    img = UploadImageForm()
    return render(request, 'contacts/login.html')


def register(request):
    reg = RegistrationForm()
    return render(request, 'contacts/register.html', {'reg': reg})


def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],
                                        email=request.POST['email'])
        user.save()
        return HttpResponseRedirect("/contacts/login")
    else:
        return render(request, 'contacts/register.html')


def logout_view(request):
    auth.logout(request)
    request.session['is_active'] = False
    # return render(request, 'contacts/login.html')
    return HttpResponseRedirect("/contacts/login")
