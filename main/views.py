
from main.models import Experience, Certification
from main.models import Project, Achievement, Testimoni, Organization
from main.forms import ProjectForm, CertificationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
import datetime
from django.http import JsonResponse 


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name='Editor').exists()

def can_edit(user):
    return user.is_authenticated and (user.is_superuser or is_editor(user))

def require_owner(user):
    if not user.is_superuser:
        raise PermissionDenied

def require_editor_or_owner(user):
    if not can_edit(user):
        raise PermissionDenied

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Jehezkiel",
        "npm": "2506611156",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Jehezkiel",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jehezkiel",
        "title_query": title_query,
        "form": ProjectForm(),
        "is_editor": is_editor(request.user),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    require_owner(request.user)
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

@login_required(login_url="/login/")
def update_project(request, project_id):
    require_editor_or_owner(request.user)
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Jehezkiel",
        "form": form,
        "is_edit": True,
        "project": project,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    require_owner(request.user)
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")



def show_certifications(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jehezkiel",
        "title_query": title_query,
        "form": CertificationForm(),
        "is_editor": is_editor(request.user),
    }
    return render(request, "certifications.html", context)

@login_required(login_url="/login/")
def create_certification(request):
    require_owner(request.user)
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

@login_required(login_url="/login/")
def update_certification(request, certification_id):
    require_editor_or_owner(request.user)
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
    title_query = request.GET.get("title", "").strip()
    certifications = Certification.objects.prefetch_related("starred_by").order_by("-issued_at")

    if title_query:
        certifications = certifications.filter(title__icontains=title_query)

    data = []
    for certification in certifications:
        starred_users = certification.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False

        data.append({
            "pk": str(certification.id),
            "fields": {
                "title": certification.title,
                "issuer": certification.issuer,
                "credential_url": certification.credential_url,
                "issued_at": certification.issued_at.isoformat(),
                "is_verified": certification.is_verified,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_certification(request, certification_id):
    require_owner(request.user)
    certification = get_object_or_404(Certification, pk=certification_id)

    if request.method == "POST":
        certification.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
        return redirect("main:show_certifications")

    return redirect("main:show_certifications")

def show_achievements(request):
    achievement_list = Achievement.objects.all()
    context = {
        'achievement_list': achievement_list
    }
    return render(request, 'achievements.html', context)

def show_testimonies(request):
    testimonies_list = Testimoni.objects.all()
    context = {
        'testimonies_list': testimonies_list
    }
    return render(request, 'testimonies.html', context)

def show_organization(request):
    organization_list = Organization.objects.all()
    context = {
        'organization_list': organization_list
    }
    return render(request, 'organization.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Jehezkiel",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Jehezkiel",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
@require_POST
def toggle_certification_star(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)

    if certification.starred_by.filter(pk=request.user.pk).exists():
        certification.starred_by.remove(request.user)
    else:
        certification.starred_by.add(request.user)

    return redirect("main:show_certifications")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_certification_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan sertifikasi."},
            status=403,
        )

    form = CertificationForm(request.POST)
    if form.is_valid():
        certification = form.save()
        return JsonResponse(
            {"message": "Sertifikasi berhasil ditambahkan.", "pk": str(certification.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)