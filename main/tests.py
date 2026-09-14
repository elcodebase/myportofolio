from django.test import TestCase, Client
from main.models import Project

class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_projects_url_is_exist_and_uses_correct_template(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_projects_display_when_data_exists(self):
        Project.objects.create(
            title="Sistem Portofolio",
            description="Aplikasi web portofolio dengan Django.",
            category="Web Development"
        )
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sistem Portofolio")
        self.assertContains(response, "Web Development")

    def test_projects_empty_state_message(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditambahkan.")