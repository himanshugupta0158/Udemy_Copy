from django.urls import path , include
from courses import views

urlpatterns = [

    path('',views.dashboard,name="dashboard"),
    path('upload/',views.upload_video,name="upload"),
    path('accounts/' , include("django.contrib.auth.urls")),
    path('register/',views.register , name="register"),
    path('register_staff/',views.register_staff , name="register_staff"),
    path('teacher_profile/',views.teacher_profile , name="teacher_profile"),
    path('student_profile/',views.student_profile , name="student_profile"),
    path('profile/' , views.profile , name = "profile"),
    path('cart/' , views.cart , name = "cart"),
    path('AddToCart/<str:course>' , views.AddToCart , name = "AddToCart"),
    path('transaction/<str:title>' , views.transaction , name = "transaction"),
    path("show_video/<str:title>", views.show_video, name="show_video"),
    path("course_category/", views.course_category, name="course_category"),
    path('check_user/' , views.check_user , name = "check_user"),
    path("buy/<str:title>", views.buy, name="buy"),


    
    

]
