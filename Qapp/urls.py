from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('signin/',views.signin,name="signin"),
    path('user/all_users/',views.all_users,name="all_users"),
    path('user/all_users/<user_name>/',views.user,name="user"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('delete_account/',views.delete_account,name="delete_account"),
	path('',views.qapp_index,name='qapp_index'),
    path('get_premium/',views.get_premium,name="get_premium"),
    path('upload_question/',views.upload_question,name="upload_question"),
    path('questions/',views.all_questions,name="all_questions"),
    path('question/<qID>/',views.question_view,name="question_view"),
    path('question/<qID>/add_answer/',views.add_answer,name="add_answer"),
]
