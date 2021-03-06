from django.shortcuts import render , redirect

from django.contrib.auth.models import User

from .models import Courses , Cart , Teacher , Student , Buy

from django.urls import reverse

from courses.forms import CustomUserCreationForm , UserManager

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login

# this is used to access of our System's FileStorageSystem to store data in designated place as defined for media.
from django.core.files.storage import FileSystemStorage

# Create your views here.

# this is Dashboard function to show all the video
def dashboard(request):
    course = Courses.objects.all()
    l = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    return render(request , 'courses/dashboard.html' , {'courses' : course , 'buyed' : l})
   

# this one show profile for currently logged in user it can be either student or teacher.
def profile(request ):
    profession = 'Teacher'
    n1 = None
    try:
        n1 = Teacher.objects.get(name = request.user.username)
    except:
        profession = 'Student'
    try:
        n1 = Student.objects.get(name = request.user.username)
    except:
        profession = 'Teacher'

    if n1 != None:
        return render(request , "courses/profile.html" , {'person' : n1 , 'profession' : profession})
    else:
        return render(request , "courses/dashboard.html" , {'msg' : "Error : profile cannot be displayed "})


# this function saves data of any video along with user's name to recognize which user buys what.
def buy(request , title):
    try:
        Buy(buyer = request.user.username , course = title).save()
        return render(request , 'courses/transaction.html' , {'product' : Courses.objects.get(title = title)})
    except:
        return render(request , "courses/dashboard.html" , {'msg' : "Error : transaction failed "})



# this function used to show the click video if it is already buyed by user. 
def show_video(request , title):
    l = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    video = Courses.objects.get(title = title)
    return render(request , 'courses/show_video.html' , {'video' : video ,'buyed' : l})


# this function is used to all video according to their category and redirect it to defined html template.
def course_category(request):
    l = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    return render(request , 'courses/course_category.html' , {'courses' : Courses.objects.all() ,'buyed' : l })
    # except:
    #     return render(request , 'courses/dashboard.html' , {'msg' : 'There is no course category exist.'})

# this video show the selected category of video from dashboard.html template
def show_selected_category(request , category):  
    l = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    return render(request , 'courses/selected_category.html' , {'courses' : Courses.objects.all(),'category' : category,'buyed' : l}) 



# this is used to upload video by only teacher.
def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.FILES['video']
        fss = FileSystemStorage()
        fss.save(video.name , video)
        description = request.POST['description']
        category = request.POST['category']
        author_name = request.POST['author']
        price = request.POST['price']
        content = Courses(title=title,description= description,category = category ,Teacher_name = author_name ,price=price ,video = video)
        content.save()
        msg = "video uploaded successfully"
        return render(request,'courses/dashboard.html' , {'msg' : msg})
    return render(request , 'courses/upload.html')


# this function is used to check whether user is teacher or student then for only teacher it allow access to upload video.
def check_user(request):
    profession = 'Teacher'
    n1 = None
    try:
        n1 = Teacher.objects.get(name = request.user.username)
    except:
        profession = 'Student'
    try:
        n1 = Student.objects.get(name = request.user.username)
    except:
        profession = 'Teacher'

    if n1 != None and profession == 'Teacher' :
        return upload_video(request)
    else:
        return render(request , "courses/dashboard.html" , {'msg' : "Student have no access to the Upload Courses."})




# this shows the data of the cart if it exist.
# In this i used try-catch b/c it was showing error that Cart is not a iterator.
def cart(request , name):
    l = set()
    course = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    for i in Cart.objects.filter(name = name ):
        course.add(Courses.objects.get(title = i.courses))
    return render(request , 'courses/cart.html' , {'courses' : course, 'buyed' : l})




# this function add cart by clicking "Add to cart" button
def AddToCart(request ,course):
    Cart(courses = course , name = request.user.username).save()
    l = set()
    course = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    for i in Cart.objects.filter(name = request.user.username):
        course.add(Courses.objects.get(title = i.courses))
    return render(request , 'courses/dashboard.html' , {'courses' : course, 'buyed' : l , 'msg' : 'Course have been added to the cart'})

# this function is used to delete data from cart (Cart database).
def DeleteFromCart(request , course):
    Cart.objects.filter(courses = course , name = request.user.username).delete()
    l = set()
    course = set()
    buyed = Buy.objects.all()
    for i in buyed :
        if request.user.username == i.buyer:
            l.add(i.course)
    for i in Cart.objects.filter(name = request.user.username):
        course.add(Courses.objects.get(title = i.courses))
    return render(request , 'courses/cart.html' , {'courses' : course, 'buyed' : l , 'msg' : 'Course have been removed form the cart'})

def DeleteAllFromCart(request):
    Cart.objects.filter(name = request.user.username).delete()
    return render(request , 'courses/cart.html' , {'msg' : 'All Courses have been removed form the cart' , 'refresh' : 'Refresh'})


"""
Note : Both student_profile and teacher_profile function automatically invokes
after either student or teacher logged in.
"""

# this is student profile information form
def student_profile(request):
    if request.method == "POST" : 
        name = request.POST['name']
        Email_address = request.POST['Email_address']
        pic = request.FILES['profile_pic']
        fss = FileSystemStorage()
        fss.save(pic.name , pic)    
        gender = request.POST['gender']
        std = Student(name = name , profile_pic = pic , gender = gender ,profession = 'Student' ,  Email_address = Email_address)
        std.save()
        return render(request , "courses/dashboard.html" ,{'prof' : std} )
    else:
        return render(request , "users/student_profile.html")


# this is Teacher's profile information form
def teacher_profile(request):
    if request.method == "POST" : 
        name = request.POST['name']
        Email_address = request.POST['Email_address']
        pic = request.FILES['profile_pic']
        fss = FileSystemStorage()
        fss.save(pic.name , pic)
        gender = request.POST['gender']
        skills = request.POST['skills']
        teacher = Teacher(name = name , profile_pic = pic , Email_address = Email_address , gender = gender , profession = 'Teacher', skills = skills)
        teacher.save()
        return render(request , "courses/dashboard.html" , {'prof' : teacher})
    else:
        return render(request , "users/teacher_profile.html")


# this is used to register students.
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
            return redirect('student_profile')
        else:
            return render(request , "users/register.html" , {'msg' : "password mismatched :  password and confirm password do not match!"})


# this is used to register teacher
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
            return redirect('teacher_profile')
        else:
            return render(request , "users/register_staff.html" , {'msg' : "password mismatched :  password and confirm password do not match!"})
