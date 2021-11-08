from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Courses , Cart , Teacher , Student
from django.urls import reverse
from courses.forms import CustomUserCreationForm , UserManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

# this is Dashboard function to show all the video
def dashboard(request):
    course = Courses.objects.all()
    return render(request , 'courses/dashboard.html' , {'courses' : course})
   

def profile(request ):
    n1 = None
    try:
        n1 = Teacher.objects.get(name = request.user.username)
    except:
        pass
    try:
        n1 = Student.objects.get(name = request.user.username)
    except:
        pass

    if n1 != None:
        return render(request , "courses/profile.html" , {'person' : n1 })
    else:
        return render(request , "courses/dashboard.html" , {'msg' : "Error : profile cannot be displayed "})

    
  
   



def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']
        description = request.POST['description']
        author_name = request.POST['author']
        price = request.POST['price']
        content = Courses(title=title,description= description, Teacher_name = author_name ,price=price ,video = video)
        content.save()
        msg = "video uploaded successfully"
        return render(request,'courses/dashboard.html' , {'msg' : msg})
    return render(request , 'courses/upload.html')


def cart(request):
    p = Cart.objects.get(std_name = request.user.username)
    products = []
    try:
        for i in p:
            products.append(Courses.objects.get(title = i.courses))
        return render(request , "courses/cart.html" , {'products':products})
    except:
        if(len(products) == 1):
            return render(request , "courses/cart.html" , {'products':Courses.objects.get(title = p.courses) , 'msg' : 'single'})
        else:
            return render(request , "courses/cart.html" , {'msg':"There is no items in your cart."})

# this function add cart by clicking "Add to cart" button
def AddToCart(request ,course):
    Cart(course , request.user.username).save()
    return render(request , 'courses/dashboard.html' , {'msg' : 'Course have been added to the cart'})

"""
Note : Both student_profile and teacher_profile function automatically invokes
after either student or teacher logged in.
"""

# this is student profile information form
def student_profile(request):
    if request.method == "POST" : 
        name = request.POST['name']
        address = request.POST['address']
        pic = request.POST['profile_pic']
        gender = request.POST['gender']
        std = Student(name = name , profile_pic = pic , gender = gender ,profession = 'Student' ,  address = address)
        std.save()
        return render(request , "courses/dashboard.html")
    else:
        return render(request , "users/student_profile.html")


# this is Teacher's profile information form
def teacher_profile(request):
    if request.method == "POST" : 
        name = request.POST['name']
        address = request.POST['address']
        pic = request.POST['profile_pic']
        gender = request.POST['gender']
        skills = request.POST['skills']
        teacher = Teacher(name = name , profile_pic = pic , address = address , gender = gender , profession = 'Teacher', skills = skills)
        teacher.save()
        return render(request , "courses/dashboard.html")
    else:
        return render(request , "users/teacher_profile.html")



    
def register(request):
    if request.method == "GET":
        return render(request , "users/register.html" , 
        {"form" : CustomUserCreationForm} )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        cred = request.POST
        username = cred['username']
        if form.is_valid():
            user = form.save()
            login(request , user)
            msg = "Signin successfully"
            return render(request , "users/student_profile.html" , {"msg" : msg})
        else:
            return render(request , "users/register.html" , {'msg' : "Invalid input in password or email!"})


def register_staff(request):
    if request.method == "GET":
        return render(request , "users/register_staff.html" , 
        {"form" : CustomUserCreationForm} )
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        conf_password = request.POST.get("password2")
        email = request.POST.get("email")
        if password == conf_password :
            user = User.objects.create_user(username, email=email, password=password)
            user.save()
            login(request , user)
            msg = "Signin successfully"
            return render(request , "users/teacher_profile.html" , {"msg" : msg})
        else:
            return render(request , "users/register_staff.html" , {'msg' : "Invalid input in password or email!"})