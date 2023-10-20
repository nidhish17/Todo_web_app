from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TodoForm, PriorityForm, RegisterUserForm, LoginForm
from .models import Todo, Priority
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django import template
# Create your views here.

register = template.Library()

# @login_required(login_url="register")
def home_page(request):
    form = TodoForm()
    todo_data = Todo.objects.all()
    priority_model = Priority.objects.all()

    #contains all the ids which has the priority
    priority_ids_lst = [i.todo_id for i in priority_model if i.priority is not None]

    sort_option = request.GET.get("sort")


    # sorted todo_data here the tasks that are done goes to the end of the list
    if request.user.is_authenticated:
        user = User.objects.get(username= request.user)
        if request.user.is_superuser:
            # Superuser should only see their own tasks
            todo_data = user.tasks.all().order_by("task_status", "start_date")
        else:
            # Regular user sees only their own tasks
            todo_data = user.tasks.all().order_by("task_status", "start_date")
    else:
        # Non-authenticated user sees no tasks
        todo_data = []

    # print(request.user)

    # user = User.objects.get(username='nidhish')
    # user_tasks = user.tasks.all()
    # print(user_tasks, "printing the user's tasks")




    # todo_data_sorted = Todo.objects.filter(user=request.user)
    if sort_option == "by_priority":
        todo_data = todo_data.order_by("task_status", "priority__priority")
    elif sort_option == "by_date":
        todo_data = todo_data.order_by("start_date")
    elif sort_option == "recent":
        todo_data = todo_data.order_by("-start_date")
    elif sort_option == "task_completed":
        todo_data = todo_data.order_by("-task_status")
    elif sort_option == "due_date":
        todo_data = todo_data.order_by("task_status", "due_date")



    context = {
        'form': form,
        'todo': todo_data,
        'todo_len': len(todo_data),
        "priority_form":PriorityForm(),
        'priority_model':priority_model,
        'priority_ids':priority_ids_lst,
    }

    return render(request, 'todo/home.html', context)

@login_required(login_url="login")
def add_task(request):

    sort_param = request.GET.get('sort')
    if request.method == 'POST':
        submitted_form = TodoForm(request.POST)
        if submitted_form.is_valid():
            task = submitted_form.save(commit=False)
            task.user = request.user
            task.save()
            if sort_param:
                homepage_url = reverse('homepage')
                return redirect(f"{homepage_url}?sort={sort_param}")


    return redirect("homepage")

@login_required(login_url="login")
def update_task_status(request, id):
    task = Todo.objects.get(id=id)
    task.task_status = not task.task_status
    task.save()
    sort_param = request.GET.get('sort')
    if sort_param:
        # Use reverse to get the URL for the "homepage" view
        homepage_url = reverse('homepage')
        # Append the 'sort' parameter to the URL
        redirect_url = f"{homepage_url}?sort={sort_param}"
        return redirect(redirect_url)
    else:
        return redirect("homepage")

@login_required(login_url="login")
def delete_task(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    sort_param = request.GET.get('sort')
    if sort_param:
        homepage_url = reverse('homepage')
        return redirect(f"{homepage_url}?sort={sort_param}")
    return redirect("homepage")

@login_required(login_url="login")
def edit_task(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(instance=task)
    # print("edit form", form)
    sort_param = request.GET.get('sort')


    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            if sort_param:
                homepage_url = reverse('homepage')
                return redirect(f"{homepage_url}?sort={sort_param}")


            return redirect("homepage")


    context = {
        'edit_form': form,
        "priority_form": PriorityForm(),
    }
    return render(request, 'todo/edit.html', context)

def set_theme(request):
    # print(request)
    if request.method == 'POST':
        request.session['theme'] = request.POST['theme']
        # print("redirecting to homepage")
        # return redirect("homepage")
        return JsonResponse({'status': 'Success'})
    return JsonResponse({'status': 'Failed'})

@login_required(login_url="login")
def set_priority(request, id):
    task = Todo.objects.get(id=id)
    sort_param = request.GET.get('sort')
    if request.method == "POST":
        priority_form = PriorityForm(request.POST)
        # print(priority_form)
        if priority_form.is_valid():
            priority = priority_form.cleaned_data['priority']
            # print(priority)
            task_priority, created = Priority.objects.get_or_create(todo=task)
            task_priority.priority = priority
            task_priority.save()
        if sort_param:
            homepage_url = reverse('homepage')
            return redirect(f"{homepage_url}?sort={sort_param}")

    return redirect("homepage")




#authentication part

def register_user(request):

    register_form = RegisterUserForm()

    if request.method == "POST":
        user_register_details = RegisterUserForm(request.POST)
        # print(user_register_details)
        if user_register_details.is_valid():
            email = user_register_details.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                # Email is not unique, display an error message
                user_register_details.add_error('email', 'This email is already in use. Please use a different email.')
            else:
                # user_details = RegisterUserForm.cleaned_data
                # print(user_register_details)
                user_register_details.save()
                # print("saved")
                return redirect("login")
    else:
        user_register_details = RegisterUserForm()

    context = {"register_form": user_register_details}


    return render(request, "todo/register.html", context)


def login_user(request):

    login_form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data= request.POST)
        # print(form)

        if form.is_valid():
            username = request.POST.get("username").lower()
            password = request.POST.get("password")
            user = authenticate(username= username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("homepage")

    else:
        form = LoginForm()

    context = {"login_form": form}

    return render(request, "todo/login.html", context)


def logout_user(request):
    auth.logout(request)
    return redirect("homepage")

def user_timezone(request):
    if request.method == "POST":
        user_timezone = request.POST.get('timezone')
        request.session['user_timezone'] = user_timezone
        return JsonResponse({'message': 'Timezone set successfully'})
    return JsonResponse({'message': 'Invalid request'}, status=400)





