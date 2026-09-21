from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, CheckboxInput

from main.models import Project, Certification

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }



class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = [
            "title",
            "issuer",
            "credential_url",
            "issued_at",
            "is_verified",
        ]

        labels = {
            "title": "Nama Sertifikasi",
            "issuer": "Diterbitkan Oleh",
            "credential_url": "URL Kredensial",
            "issued_at": "Tanggal Terbit",
            "is_verified": "Sudah Terverifikasi?",
        }

        widgets = {
            "title": TextInput(attrs={"placeholder": "Belajar Fundamental Back-End dengan Django", "maxlength": 255}),
            "issuer": TextInput(attrs={"placeholder": "Dicoding Indonesia"}),
            "credential_url": URLInput(attrs={"placeholder": "https://www.dicoding.com/certificates/..."}),
            "issued_at": DateInput(attrs={"type": "date"}),
            "is_verified": CheckboxInput(),
        }