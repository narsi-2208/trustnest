from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .models import Mentor, CareerSwitcher, User

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try logging in as Mentor
        try:
            mentor = Mentor.objects.get(email=email)
            if mentor.password == password:
                request.session['mentor_id'] = mentor.id
                request.session['mentor_name'] = mentor.full_name
                return redirect('index') 
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except Mentor.DoesNotExist:
            pass  # Not a mentor, try career switcher

        # Try logging in as Career Switcher
        try:
            consumer = CareerSwitcher.objects.get(email=email)
            if consumer.password == password:
                request.session['consumer_id'] = consumer.id
                request.session['consumer_name'] = consumer.full_name
                return redirect('index') 
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except CareerSwitcher.DoesNotExist:
            return render(request, 'login.html', {'error': 'User not found'})

    return render(request, 'login.html')


def signup_provider(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        background = request.POST.get('background')
        current_role = request.POST.get('current_role')
        linkedin = request.POST.get('linkedin')
        bio = request.POST.get('bio')
        offers_mentoring = request.POST.get('offers_mentoring') == 'Yes'

        Mentor.objects.create(
            full_name=full_name,
            email=email,
            password=password,
            background=background,
            current_role=current_role,
            linkedin=linkedin,
            bio=bio,
            offers_mentoring=offers_mentoring
        )

        return redirect(reverse('login'))

    return render(request, 'signup-provider.html')


def signup_consumer(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        background = request.POST.get('background')
        target_role = request.POST.get('target_role')
        reason = request.POST.get('reason')

        CareerSwitcher.objects.create(
            full_name=full_name,
            email=email,
            password=password,
            current_background=background,
            target_role=target_role,
            motivation=reason
        )

        return redirect(reverse('login'))

    return render(request, 'signup-consumer.html')


def index(request):
    mentors = Mentor.objects.all()
    return render(request, 'index.html', {'mentors': mentors})



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        mentor_exists = Mentor.objects.filter(email=email).exists()
        consumer_exists = CareerSwitcher.objects.filter(email=email).exists()

        if mentor_exists or consumer_exists:
            # You can add logic to send email here
            return render(request, 'forgot-password.html', {
                'message': 'If this email is registered, reset instructions will be sent.'
            })
        else:
            return render(request, 'forgot-password.html', {
                'error': 'This email is not registered.'
            })

    return render(request, 'forgot-password.html')

def mentor_detail(request, id):
    mentor = get_object_or_404(Mentor, id=id)
    return render(request, 'detail.html', {'mentor': mentor})


