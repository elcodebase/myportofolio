from django.urls import path
from main.views import (
    show_main, show_experience, toggle_star,
    show_projects, create_project, get_projects_json, delete_project, update_project,
    show_certifications, create_certification, update_certification, toggle_certification_star, create_project_ajax,
    delete_certification, get_certifications_json, show_achievements, show_testimonies, show_organization, register, login_user, logout_user
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('projects/', show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),

    #untuk sertifikasi
    path("certifications/", show_certifications, name = "show_certifications"),
    path("certifications/add/", create_certification, name="create_certification"),
    path("certifications/<uuid:certification_id>/edit/", update_certification, name="update_certification"),
    path("certifications/<uuid:certification_id>/delete/", delete_certification, name="delete_certification"),
    path("api/certifications/", get_certifications_json, name="get_certifications_json"),
    path("achievement/", show_achievements, name = 'show_achievements'),
    path("testimonies/", show_testimonies, name = 'show_testimonies'),
    path("organization/", show_organization, name = 'show_organization'),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"), 

    path("projects/<uuid:project_id>/edit/", update_project, name="update_project"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("certifications/<uuid:certification_id>/star/", toggle_certification_star, name="toggle_certification_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
 
]
