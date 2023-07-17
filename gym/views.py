from django.shortcuts import render
from gymproduct.models import EnquiryModels
from django.core.mail import send_mail,EmailMultiAlternatives
import random


def HomePage(request):
    return render(request,'newHeader.html')
def AboutUs(request):
    return render(request,'About.html')
def ourProducts(request):
    return render(request,'Ourproducts.html')
def Enquiry(request):
    n = ""
    x= ''
    if request.method=="POST":
        gender = request.POST.get("gender")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        age  = request.POST.get('age')
        city = request.POST.get('city')
        packages = request.POST.get('packages')
        en = EnquiryModels(Gender=gender,Name=name,Age=age,Phone=phone,email_address=email, City=city, our_packages=packages)
        en.save()
        x = random.randint(1000,9999)
        n = "congratulation! You have successfully booked your memebership.Your appliction no. is {}".format(x)
        subject='MEMBERSHIP'
        message= '''<p>Thank you for Visiting us.Hey,<b>{}</b> You have succesfully booked your <b>{}</b> package. 
        Your application no. is <b>{}</b>.
        Welcome to the Xtream Fitness</b>,
        Our trainers are ready to help you get in the best 
        shape of your life.</p>'''.format(name,packages,x)
        from_email='xtreamfitness21@gmail.com'
        recipient_list=['sagar885941@gmail.com']
        msg=EmailMultiAlternatives(subject,message,from_email,recipient_list)
        msg.content_subtype='html'
        msg.send()
        fail_silently=False
     
    return render(request,'enquiry.html',{'n':n})

def Calculator(request):
    c=''
    d=''
    f=0
    try:
         if request.method=='POST':
            n1=eval(request.POST.get('feet'))
            n2=eval(request.POST.get('inches'))
            n3=eval(request.POST.get('weight'))
            c=((n1*30.48)+(n2*2.54))
            d= float((n3)/((c*.01)**2))
            f=('%.2f' % d)
    except:
        pass
    return render(request,'Bmi.html',{'f':f})