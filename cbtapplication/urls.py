from django.urls import path
from . import views

urlpatterns = [
    path("exam/<slug:exam_subject>", views.exam_page, name="exam-page"),
    path("student/login", views.student_login, name="student-login-page"),
    path("student/dashboard", views.student_dashboard, name="student-dashboard-page"),
    path("logout", views.logout_view, name="logout"),
    path("", views.moderator_login, name="moderator-login-page"),
    path("moderator/add-user", views.add_user, name="add-user-page"),
    path("moderator/dashboard", views.moderator_dashboard, name="moderator-dashboard-page"),
    path("moderator/check-result", views.check_result, name="result-page"),
    path("moderator/manage-exam", views.manage_exam, name="manage-exam-page"),
]