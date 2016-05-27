from django.shortcuts import render
from blog.forms import Blogeditor
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            request.session['is_active'] = True
            request.session['user_id'] = user.id
            # Redirect to a success page.
            # return HttpResponseRedirect("sdfghjkl")
            #return HttpResponse(user.email)

            #fname = user.
            #return render(request, 'blog/list', )
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            # return HttpResponseRedirect("sfsdgsdgsggggggggggggg")
            return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],
                                        email=request.POST['email'])
        user.save()
        # return HttpResponseRedirect("/login")
        return HttpResponse(user.id)
    else:
        return render(request, 'blog/register.html')

#@login_required(login_url="/login/")
def newblog(request):
    #blog_form = Blogeditor()
    #return render(request, 'blog/blog.html', {'blog_form': blog_form})
    return render(request, 'blog/list.html', {'use': User.objects.get(id=request.session['user_id'])})

def saveblog(request):
    if request.method == 'POST':
        text = request.POST.get('blog')
        blogcont = Blog(content=text)
        blogcont.save()

    return HttpResponse()
    #return render(request, 'blog/list.html', {'bloglist': Blog.objects.values()})

@login_required(login_url="/login/")
def user_edit(request, use_id):
    #if request.method == "POST":
    #    print "sdfsdf"
    #else:
        return render(request, 'blog/user_edit.html', {'use': User.objects.get(id=use_id)})