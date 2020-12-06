from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Contact
# Create your views here.

def contact(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(
                car_id=car_id, user_id=user_id
            )

            if has_contacted:
                messages.error(request, ' You have already made an inquery')
                return redirect('/cars/detail/'+ car_id)


        contact = Contact(
            first_name=first_name, last_name=last_name, car_id=car_id,
            car_title=car_title, user_id=user_id, city=city, state=state,
            email=email, phone=phone, message=message,
        )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New car inquiry',
            'Here is the message test.',
            'bergerh2022@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'You request has been submitted')
        return  redirect('/cars/detail/'+ car_id)
