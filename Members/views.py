from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Subject, Topic, Note #GetClass
from .forms import SubjectForm, TopicForm, NoteForm #ClassForm
from .permissions import allowed_users

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    subject_var = Subject.objects.values().all()
    context = {
        'user' : user,
        'subject' : subject_var,
    }
    return render(request, 'dashboard.html', context)

'''
@login_required(login_url='login')
def get_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if GetClass.objects.all().values()
    else:
        form = ClassForm
    return render(request, 'get_class.html', {'form' : form})
'''

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_panel(request):
    user = request.user
    subject_var = Subject.objects.values().all()
    context = {
        'user' : user,
        'subject' : subject_var,
    }
    return render(request, 'admin_panel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SubjectForm
    return render(request, 'add_subject.html', {'form' : form})

@login_required(login_url='login')
def edit_subject(request):
    return render(request, 'edit_subject.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TopicForm
    return render(request, 'add_topic.html', {'form' : form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NoteForm
    return render(request, 'add_note.html', {'form' : form})

@login_required(login_url='login')
def topic_view(request, id):
    subject_id = Subject.objects.get(id=id)
    topic_var = Topic.objects.all().values().filter(get_subject_id=subject_id.id)
    context = {
        'topic' : topic_var,
        'subject' : subject_id
    }
    return render(request, 'topic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_topic(request, id):
    subject_id = Subject.objects.get(id=id)
    topic_var = Topic.objects.all().values().filter(get_subject_id=subject_id.id)
    context = {
        'topic' : topic_var,
        'subject' : subject_id
    }
    return render(request, 'admin_topic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_note(request, id):
    topic_id = Topic.objects.get(id=id)
    note_var = Note.objects.all().values().filter(get_topic_id=topic_id.id)
    context = {
        'notes' : note_var,
        'topic' : topic_id
    }
    return render(request, 'admin_note.html', context)

@login_required(login_url='login')
def note_view(request, id):
    topic_id = Topic.objects.get(id=id)
    note_var = Note.objects.all().values().filter(get_topic_id=topic_id.id)
    context = {
        'notes' : note_var,
        'topic' : topic_id
    }
    return render(request, 'note.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')