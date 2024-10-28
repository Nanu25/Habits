from datetime import timezone
from sqlite3 import IntegrityError

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from habits.models import User, Habit
from habits.templatetags.custom_filters import get_badge


# Create your views here.

def index(request):
    # habits = Habit.objects.all()
    habits = None
    return render(request, "habits/index.html", {
        "habits": habits
    })


def main_page(request):
    # Get all habits for the current user
    habits = Habit.objects.filter(user=request.user)

    total_completed = 0
    for habit in habits:
        if habit.times_completed >= 30:
            total_completed += 1
        if habit.times_completed < 10:
            habit.status = "Habit at the beginning"
        elif habit.times_completed < 20:
            habit.status = "Keep going"
        elif habit.times_completed < 30:
            habit.status = "Almost there"
        else:
            habit.status = "Congrats, you built a habit!"


    user_badges = get_badge(total_completed)

    return render(request, "habits/main_page.html", {
        "habits": habits,
        "user_badges": user_badges
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
        private = request.POST.get("private") == "on"
        new_habit = Habit(user=request.user, habit=habit, description=description, status=status, private=private)
        new_habit.save()
        return redirect('main_page')  # Redirect to a page of your choice after adding the habit

    habits = Habit.objects.filter(user=request.user)
    total_completed = 0
    for habit in habits:
        if habit.times_completed >= 30:
            total_completed += 1

    user_badges = get_badge(total_completed)
    return render(request, "habits/add_habit.html", {
        "user_badges": user_badges
    })


@csrf_exempt  # Use this only if you are handling CSRF manually in the fetch request
def mark_done(request, habit_id):
    if request.method == 'POST':
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)

        # Increment the completion count
        habit.times_completed += 1
        habit.completed = True  # Mark as completed
        if habit.times_completed == 30:
            habit.status = "Habit completed"
        habit.save()

        # Return JSON response
        return JsonResponse({
            'completed': habit.completed,
            'times_completed': habit.times_completed,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def top_habits(request):
    top_habit = (
        Habit.objects
        .filter(private=False)  # Filter to include only non-private habits
        .values('habit')
        .annotate(habit_count=Count('habit'))
        .order_by('-habit_count')[:6]
    )

    habits = Habit.objects.filter(user=request.user)
    total_completed = 0
    for habit in habits:
        if habit.times_completed >= 30:
            total_completed += 1

    user_badges = get_badge(total_completed)
    return render(request, 'habits/top_habits.html', {
        'top_habits': top_habit,
        'user_badges': user_badges
    })





