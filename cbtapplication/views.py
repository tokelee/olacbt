from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from cbtapplication.forms.registration_forms import UserAdditionalDetailsForm, UserForm
from django.contrib import messages
from cbtapplication.models import UserDetail, ExamSubject, Result, Question
from django.contrib.auth.models import User
from django.db.models import Q
import math
from random import shuffle

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/student/login")


@login_required(login_url="/student/login")
def exam_page(request, exam_subject):
    exam_subject_id =  math.floor(int(str(exam_subject).split("-")[-1])/89)
    questions_db = Question.objects.all().filter(exam_subject_id=exam_subject_id)
    questions_db = list(questions_db)
    shuffle(questions_db)
    questions=[]
    n = 0
    for i in questions_db:
        n+=1
        question_prop = {"question_no": n, "question":i}
        questions.append(question_prop)
    mark = 0
    remark = ""
    if request.method == "POST":
        for items in list(request.POST.values())[1:]:
            correct =  str(items).lower().split("-")[0] == str(items).lower().split("-")[-1]
            mark = mark+1.5 if correct else mark+0
        check_duplicate = Result.objects.filter(exam_subject_id=exam_subject_id, user=request.user).first()
        if check_duplicate is None:
            if(mark > 48):
                remark = "Excellent"
            elif(mark > 41):
                remark = "Very good"
            elif mark > 34:
                remark = "Good"
            elif mark > 27:
                remark = "Fair"
            else:
                remark = "Poor"
            result = Result.objects.create(exam_subject_id=exam_subject_id, user=request.user, score=mark, grade=remark)
            result.save()
        return HttpResponseRedirect("/student/dashboard")
    subject = questions_db[0]
    subject_name = subject.exam_subject.subject.name
    class_year = subject.exam_subject.class_year
    department = request.user.userdetail.department
    return render(request, "cbtapplication/student_pages/exam-page.html", {"question":questions[:10], "subject_name":subject_name, "class_year":class_year, "department":department})

def student_login(request):
    if request.method == "POST":
        userID = request.POST['user-id']
        password = request.POST['password']
        user = authenticate(request, username=str(userID).upper(), password=str(password).lower())
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login Successful")
            return HttpResponseRedirect("/student/dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password.")
    return render(request, "cbtapplication/student_pages/student-login.html")

@login_required(login_url="/student/login")
def student_dashboard(request):
    current_user = request.user
    current_user_dept = current_user.userdetail.department
    current_user_class = current_user.userdetail.class_year
    result = Result.objects.filter(user=current_user)
    exam_subject = ExamSubject.objects.filter(Q(department="all") | Q(department=current_user_dept), class_year=current_user_class)
    done_exams = [i.exam_subject.subject.name for i in result]
    exams = []
    for i in exam_subject:
        if(i.subject.name in done_exams):
            exam_prop = {"id": i.id,"subject":i.subject.name, "class":i.class_year, "department":i.department, "isActive":False}
            exams.append(exam_prop)
        else:
            exam_prop = {"id": i.id, "subject":i.subject.name, "class":i.class_year, "department":i.department, "isActive":True}
            exams.append(exam_prop)
    return render(request, "cbtapplication/student_pages/dashboard.html", {"exam_subject":exams})


# Moderator pages
def moderator_login(request):
    if request.method == "POST":
        userID = request.POST['user-id']
        password = request.POST['password']
        user = authenticate(request, username=str(userID).lower(), password=str(password).lower())
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login Successful")
            return HttpResponseRedirect("/moderator/dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password.")
    return render(request, "cbtapplication/moderator_pages/admin-login.html")


@login_required("")
def add_user(request):
    if request.method == "POST":
        form1 = UserForm(request.POST)
        form2 = UserAdditionalDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            username = form1.cleaned_data['username']
            class_year = form2.cleaned_data['class_year']
            department = form2.cleaned_data['department']
            role = form2.cleaned_data['role']
            dob = form2.cleaned_data['dob']
            is_computer_literate = form2.cleaned_data['is_computer_literate']
            password = str(last_name).lower()+"pass"
            if str(role).lower() == "moderator":
                user = User.objects.create_user(username=str(username).upper(),last_name=str(last_name).capitalize(), first_name=str(first_name).capitalize(), password=str(password).lower(), is_staff=True, is_superuser=True)
                user.save()
            else:
                user = User.objects.create_user(username=str(username).upper(),last_name=str(last_name).capitalize(), first_name=str(first_name).capitalize(), password=str(password).lower())
                user.save()
                userDetails = UserDetail.objects.create(role=role, department=department, class_year=class_year, user=user, dob=dob, is_computer_literate=is_computer_literate)
                userDetails.save()
            messages.add_message(request, messages.SUCCESS, f"""Successfully created an account for {str(first_name).capitalize()} 
                                 \n Username: {str(username).upper()} 
                                 \n Password: {password}""")
            form1 = UserForm()
            form2 = UserAdditionalDetailsForm()
    else:
        form1 = UserForm()
        form2 = UserAdditionalDetailsForm()
    return render(request, "cbtapplication/moderator_pages/add-user.html", {"form1": form1, "form2": form2})

@login_required("")
def moderator_dashboard(request):
    results = Result.objects.all().order_by("-created_at")[:5]
    return render(request, "cbtapplication/moderator_pages/dashboard.html", {"results":results})

@login_required("")
def manage_exam(request):
    exam = ExamSubject.objects.all()
    return render(request, "cbtapplication/moderator_pages/manage-exam.html", {"exams": exam})

@login_required("")
def check_result(request):
    class_filter = request.GET.get("class", "")
    department_filter = request.GET.get("department", "")
    if((class_filter != "")):
        results = Result.objects.all().filter(exam_subject__class_year=class_filter).order_by("-score")
    elif((department_filter is not "")):
        results = Result.objects.all().filter(Q(exam_subject__department=department_filter) | Q(exam_subject__department="all")).order_by("-score")
    elif((class_filter != "") and (department_filter is not "")):
        results = Result.objects.all().filter(Q(exam_subject__department=department_filter) | Q(exam_subject__department="all"), exam_subject__class_year=class_filter).order_by("-score")
    else:
        results = Result.objects.all().filter().order_by("-score")
    return render(request, "cbtapplication/moderator_pages/result-page.html", {"results":results})