from django.shortcuts import render, HttpResponse
from student_app.models import StudentModel
from student_app.student import *



def add_student(request):
    from student_app.forms import AddStudentForm

    form = AddStudentForm(request.POST or None)

    if form.is_valid():

        post = StudentModel(name=form.cleaned_data['name'],
                            grades=form.cleaned_data['grades'],
                            average_grade=form.cleaned_data['average']
                            )

        post.save()

        context = {
            'post': post
                    }

        return render(request,
                      template_name='new_entry.html',
                      context=context)

    context = {
        'form': form,
    }

    return render(request,
                  template_name='student.html',
                  context=context)





def get_all_students(request):

    context = {
        'posts': StudentModel.objects.all()
    }

    return render(request,
                  template_name='all_students.html',
                  context=context)


def get_student(request,post_id):

    context = {
        'posts': StudentModel.objects.get(id=post_id)
    }

    return render(request,
                  template_name='new_entry.html',
                  context=context)

#Izveidot view, kas pie metodes GET renderēs HTML formu, kurā ir nepieciešams ievadīt
# name, grades (grades ir string, piemēram 7,10,4). Kad forma tiek
# iesniegta (metode POST), tiek veidots jauns klases Student objekcts.
# Datubāzei tiek pievienots jauns ieraksts (ar StudentModel).
# Forma tiek parādīta uz '/student/add'.


