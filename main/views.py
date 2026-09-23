from django.shortcuts import render

from main.models import Experience, Certification
from main.models import Project, Achievement, Testimoni, Organization
from main.forms import ProjectForm, CertificationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def show_main(request):
    context = {
        "name": "Jehezkiel",
        "npm": "2506611156",
        "study_program": "S1 Sistem Informasi ",
        "bio": (
            "Mahasiswa Sistem Informasi  Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Jehezkiel",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jehezkiel",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Jehezkiel",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")



def show_certifications(request):
    json_response = get_certifications_json(request)
    certifications = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    certifications = [certification.object for certification in certifications]

    context = {
        "name": "Jehezkiel",
        "certification_list": certifications,
    }
    return render(request, "certifications.html", context)


def create_certification(request):
    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikasi baru berhasil ditambahkan!")
        return redirect("main:show_certifications")

    context = {
        "name": "Jehezkiel",
        "form": form,
        "is_edit": False,
    }
    return render(request, "certifications_form.html", context)


def update_certification(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)
    form = CertificationForm(request.POST or None, instance=certification)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikasi berhasil diperbarui!")
        return redirect("main:show_certifications")

    context = {
        "name": "Jehezkiel",
        "form": form,
        "is_edit": True,
        "certification": certification,
    }
    return render(request, "certifications_form.html", context)


def get_certifications_json(request):
    certifications = Certification.objects.all()
    certifications_json = serializers.serialize("json", certifications)
    return HttpResponse(certifications_json, content_type="application/json")


def delete_certification(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)

    if request.method == "POST":
        certification.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
        return redirect("main:show_certifications")

    return redirect("main:show_certifications")

def show_achievements(request):
    achievement_list = Achievement.objects.all()
    context = {
        'achievement': achievement_list
    }
    return render(request, 'achievements.html', context)

def show_testimonies(request):
    testimonies_list = Testimoni.objects.all()
    context = {
        'testimonies': testimonies_list
    }
    return render(request, 'testimonies.html', context)

def show_organization(request):
    organization_list = Organization.objects.all()
    context = {
        'organization': organization_list
    }
    return render(request, 'organization.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("main:show_main")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)