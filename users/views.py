# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse
# from django.contrib.auth.hashers import make_password
# from .models import Mentor, CareerSwitcher, User

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Try logging in as Mentor
#         try:
#             mentor = Mentor.objects.get(email=email)
#             if mentor.password == password:
#                 request.session['mentor_id'] = mentor.id
#                 request.session['mentor_name'] = mentor.full_name
#                 return redirect('index') 
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid password'})
#         except Mentor.DoesNotExist:
#             pass  # Not a mentor, try career switcher

#         # Try logging in as Career Switcher
#         try:
#             consumer = CareerSwitcher.objects.get(email=email)
#             if consumer.password == password:
#                 request.session['consumer_id'] = consumer.id
#                 request.session['consumer_name'] = consumer.full_name
#                 return redirect('index') 
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid password'})
#         except CareerSwitcher.DoesNotExist:
#             return render(request, 'login.html', {'error': 'User not found'})

#     return render(request, 'login.html')


# def signup_provider(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         password = make_password(request.POST.get('password'))
#         background = request.POST.get('background')
#         current_role = request.POST.get('current_role')
#         linkedin = request.POST.get('linkedin')
#         bio = request.POST.get('bio')
#         offers_mentoring = request.POST.get('offers_mentoring') == 'Yes'

#         Mentor.objects.create(
#             full_name=full_name,
#             email=email,
#             password=password,
#             background=background,
#             current_role=current_role,
#             linkedin=linkedin,
#             bio=bio,
#             offers_mentoring=offers_mentoring
#         )

#         return redirect(reverse('login'))

#     return render(request, 'signup-provider.html')


# def signup_consumer(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         password = make_password(request.POST.get('password'))
#         background = request.POST.get('background')
#         target_role = request.POST.get('target_role')
#         reason = request.POST.get('reason')

#         CareerSwitcher.objects.create(
#             full_name=full_name,
#             email=email,
#             password=password,
#             current_background=background,
#             target_role=target_role,
#             motivation=reason
#         )

#         return redirect(reverse('login'))

#     return render(request, 'signup-consumer.html')


# def index(request):
#     mentors = Mentor.objects.all()
#     return render(request, 'index.html', {'mentors': mentors})



# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

#         mentor_exists = Mentor.objects.filter(email=email).exists()
#         consumer_exists = CareerSwitcher.objects.filter(email=email).exists()

#         if mentor_exists or consumer_exists:
#             # You can add logic to send email here
#             return render(request, 'forgot-password.html', {
#                 'message': 'If this email is registered, reset instructions will be sent.'
#             })
#         else:
#             return render(request, 'forgot-password.html', {
#                 'error': 'This email is not registered.'
#             })

#     return render(request, 'forgot-password.html')

# def mentor_detail(request, id):
#     mentor = get_object_or_404(Mentor, id=id)
#     return render(request, 'detail.html', {'mentor': mentor})



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Helper

# USER (Consumer) Signup View
def signup_consumer(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('location')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup-consumer')

        hashed_password = make_password(password)

        User.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password_hash=hashed_password,
            location=location
        )
        messages.success(request, "Consumer registered successfully!")
        return redirect('login')

    return render(request, 'signup-consumer.html')


def signup_provider(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        location = request.POST.get('location')
        skills = request.POST.getlist('skills')  # use checkbox or multiselect
        experience_years = request.POST.get('experience_years')
        languages = request.POST.getlist('languages')  # use checkbox or multiselect
        documents = request.POST.get('documents')  # JSON as text (or handle with JS)
        availability = request.POST.get('availability')  # JSON as text
        password = request.POST.get('password')

        if Helper.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup-provider')

        hashed_password = make_password(password)

        Helper.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            gender=gender,
            age=int(age),
            location=location,
            skills=skills,
            experience_years=int(experience_years),
            languages=languages,
            documents=documents,
            availability=availability,
            password_hash=hashed_password
        )
        messages.success(request, "Provider registered successfully!")
        return redirect('login')

    return render(request, 'signup-provider.html')

# LOGIN View (shared)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try User
        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password_hash):
            # Save session or token as needed
            messages.success(request, f"Welcome, {user.full_name}!")
            return redirect('dashboard')  # or home

        # Try Helper
        helper = Helper.objects.filter(email=email).first()
        if helper and check_password(password, helper.password_hash):
            messages.success(request, f"Welcome, {helper.full_name}!")
            return redirect('dashboard')  # or home

        messages.error(request, "Invalid credentials.")
        return redirect('login')

    return render(request, 'login.html')


