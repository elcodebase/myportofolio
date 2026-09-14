from django.db import migrations


def add_projects(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    projects = [
        {
            "title": "Sistem Portofolio Pribadi",
            "description": (
                "Website portofolio pribadi berbasis Django untuk menampilkan "
                "profil, pengalaman, dan proyek. Dibangun dengan struktur MTV "
                "Django serta styling custom CSS tanpa framework tambahan."
            ),
            "category": "Web Development",
        },
        {
            "title": "Sistem Manajemen Tugas Kuliah",
            "description": (
                "Aplikasi pencatat tugas kuliah dengan fitur pengingat deadline, "
                "kategori mata kuliah, dan status pengerjaan. Dibuat sebagai "
                "latihan penerapan CRUD pada Django."
            ),
            "category": "Web Development",
        },
        {
            "title": "Bot Absensi Otomatis",
            "description": (
                "Script Python yang mengotomatisasi pengisian absensi kelas "
                "menggunakan Selenium, lengkap dengan penjadwalan otomatis "
                "setiap awal jam pelajaran."
            ),
            "category": "Automation",
        },
        {
            "title": "Aplikasi Pencatat Keuangan Mahasiswa",
            "description": (
                "Aplikasi sederhana untuk mencatat pemasukan dan pengeluaran "
                "harian mahasiswa, dilengkapi ringkasan bulanan dan grafik "
                "pengeluaran per kategori."
            ),
            "category": "Mobile Development",
        },
        {
            "title": "Landing Page UKM Lokal",
            "description": (
                "Landing page responsif untuk UKM lokal yang menampilkan katalog "
                "produk, informasi kontak, dan integrasi tombol pemesanan "
                "langsung ke WhatsApp."
            ),
            "category": "UI/UX & Frontend",
        },
    ]

    for data in projects:
        Project.objects.get_or_create(
            title=data["title"],
            defaults={
                "description": data["description"],
                "category": data["category"],
            },
        )


def remove_projects(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    titles = [
        "Sistem Portofolio Pribadi",
        "Sistem Manajemen Tugas Kuliah",
        "Bot Absensi Otomatis",
        "Aplikasi Pencatat Keuangan Mahasiswa",
        "Landing Page UKM Lokal",
    ]
    Project.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_project"),
    ]

    operations = [
        migrations.RunPython(add_projects, remove_projects),
    ]
