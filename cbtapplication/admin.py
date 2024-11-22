from django.contrib import admin
from .models import ExamSubject, Instruction, Question, Result, Subject, UserDetail

@admin.register(ExamSubject)
class ExamSubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    pass

