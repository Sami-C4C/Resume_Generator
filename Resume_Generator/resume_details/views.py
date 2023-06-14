from django.shortcuts import render, get_object_or_404, redirect
from .models import Resume_Detail
import pdfkit
from django.http import HttpResponse
from django.template import loader

from .models import Resume_Detail
from .forms import ResumeForm
import io


def home(request):
    return render(request, 'resume_details/home.html')


def save_resume(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        country = request.POST.get("country")
        photo = request.FILES.get("photo")
        region = request.POST.get("region")
        occupation = request.POST.get("occupation")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        degree = request.POST.get("degree")
        summary = request.POST.get("summary")
        education = request.POST.get("education")
        work_experience = request.POST.get("work_experience")
        skills = request.POST.get("skills")
        hobbies = request.POST.get("hobbies")

        resume_fields = Resume_Detail(
            first_name=first_name,
            last_name=last_name,
            country=country,
            photo=photo,
            region=region,
            occupation=occupation,
            dob=dob,
            email=email,
            phone=phone,
            degree=degree,
            summary=summary,
            education=education,
            work_experience=work_experience,
            skills=skills,
            hobbies=hobbies,
        )
        resume_fields.save()
    return render(request, 'resume_details/formular.html')


def resume_layout(request, id):
    user_resume_details = Resume_Detail.objects.get(pk=id)

    # Create the absolute URL
    photo_url = request.build_absolute_uri(user_resume_details.photo.url)

    layout = loader.get_template('resume_details/layout.html')
    context = {
        'user_resume_details': user_resume_details,
        'photo_url': photo_url,
    }
    html_slide = layout.render(context)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8 ',
        'no-stop-slow-scripts': True,
        'debug-javascript': True,
    }
    pdf_slide = pdfkit.from_string(html_slide, False, options)
    response = HttpResponse(pdf_slide, content_type='application/pdf')

    # Constructing file name
    file_name = 'resume_{}_{}.pdf'.format(user_resume_details.first_name, user_resume_details.last_name)

    # Adding the filename to the Content-Disposition header
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)

    return response


def show_All_Resumes(request):
    user_resume_details = Resume_Detail.objects.all()
    return render(request, 'resume_details/CVs_Pool.html', {'user_resume_details': user_resume_details})


def resume_delete(request, id):
    resume = get_object_or_404(Resume_Detail, id=id)
    if request.method == "POST":
        resume.delete()
        return redirect('resumes_pool')  # Name of the URL where to redirect after a successful deletion
    return render(request, 'resume_details/delete_resume.html', {'user_resume_details': resume})


def resume_edit(request, id):
    resume = get_object_or_404(Resume_Detail, id=id)
    user = Resume_Detail.objects.get(pk=id)

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resumes_pool')  # Name of the URL where to redirect after a successful update
    else:
        form = ResumeForm(instance=resume)

    # Send the user object as context to the template.
    return render(request, 'resume_details/edit_resume.html', {'form': form, 'user_resume_details': user})
