import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    def __str__(self):
        return self.title

class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    credential_url = models.URLField(blank=True)
    issued_at = models.DateField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.issuer}"

class Achievement(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 200)
    description = models.TextField()

    class Level(models.TextChoices):
        CAMPUS = 'campus', 'Campus'
        NATIONAL = 'national', 'National'
        INTERNATIONAL = 'international', 'International'

    level = models.CharField(
        max_length = 20,
        choices = Level.choices,
        default = Level.CAMPUS,
    )

    @property
    def is_top_tier(self):
        return self.level in [self.Level.National, self.Level.International]

    def __str__(self):
        return self.title

class Testimoni(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()

    class Category(models.TextChoices):
        DOSEN = 'dosen', 'Dosen'
        TEMAN = 'teman', 'Teman'
        KELUARGA = 'keluarga', 'Keluarga'

    category = models.CharField(
        max_length = 20,
        choices = Category.choices,
        default = Category.TEMAN,
    )

    @property
    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length = 200)

    class Level(models.TextChoices):
        FAKULTAS = 'fakultas', 'Fakultas'
        EKSTERNAL = 'eksternal', 'Eksternal'
        KAMPUS = 'kampus', 'Kampus'

    level = models.CharField(
        max_length = 20,
        choices = Level.choices,
        default = Level.FAKULTAS,

    )

    def __str__(self):
        return self.name

        