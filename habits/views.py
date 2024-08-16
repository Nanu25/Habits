from sqlite3 import IntegrityError

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from habits.models import User, Habit


# Create your views here.

def index(request):
    # habits = Habit.objects.all()
    habits = None
    return render(request, "habits/index.html", {
        "habits": habits
    })
def main_page(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habits/main_page.html", {
        "habits": habits
    })
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main_page"))
        else:
            return render(request, "habits/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "habits/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "habits/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "habits/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("main_page"))
    else:
        return render(request, "habits/register.html")


@login_required
def add_habit(request):
    if request.method == "POST":
        habit = request.POST.get("habit")
        description = request.POST.get("description")
        status = "Habit at the beginning"
        new_habit = Habit(user=request.user, habit=habit, description=description, status=status)
        new_habit.save()
        return redirect('main_page')  # Redirect to a page of your choice after adding the habit
    return render(request, "habits/add_habit.html")


@csrf_exempt  # Use this only if you are handling CSRF manually in the fetch request
def mark_done(request, habit_id):
    if request.method == 'POST':
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)

        # Increment the completion count
        habit.times_completed += 1
        habit.completed = True  # Mark as completed
        habit.save()

        # Return JSON response
        return JsonResponse({
            'completed': habit.completed,
            'times_completed': habit.times_completed,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
