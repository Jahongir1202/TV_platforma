from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_sha256$"):  # Agar parol xashlanmagan bo‘lsa
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


from urllib.parse import urlparse, parse_qs

class Ertaklar(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Ertaklar.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None

class WatchedVideo(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Ertaklar, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"
class Multfilmlar(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Multfilmlar.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedMultfilm(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Multfilmlar, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"


class Qoshiqlar(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Qoshiqlar.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedQoshiqlar(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Qoshiqlar, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"


class Qiziqari_Matematika(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Qiziqari_Matematika.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedMatematika(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Qiziqari_Matematika, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"

class Ingliztili(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Ingliztili.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedIngliztili(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Ingliztili, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"




class Badantarbiya(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Badantarbiya.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedBadantarbiya(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Badantarbiya, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"

class Rasmlar(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    order = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            last_video = Rasmlar.objects.order_by('-order').first()
            self.order = (last_video.order + 1) if last_video else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"

    def embed_video(self):
        """YouTube URL'dan video ID ni ajratib olib, iframe uchun URL hosil qiladi."""
        from urllib.parse import urlparse, parse_qs

        parsed_url = urlparse(self.video_url)
        video_id = None

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v", [None])[0]
        elif parsed_url.hostname in ["youtu.be"]:
            video_id = parsed_url.path.lstrip("/")

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
class WatchedRasmlar(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Rasmlar, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({'Ko‘rilgan' if self.watched else 'Ko‘rilmagan'})"


from django.db import models

class Ariza(models.Model):
    full_name = models.CharField(max_length=255)  # Ism
    phone_number = models.CharField(max_length=15)  # Telefon raqam
    message = models.TextField(blank=True, null=True)  # Ixtiyoriy xabar
    created_at = models.DateTimeField(auto_now_add=True)  # Qachon qoldirilgani

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"


class TestQuestion(models.Model):
    question_text = models.TextField()  # Savol matni
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[(1, "A"), (2, "B"), (3, "C"), (4, "D")])  # To‘g‘ri variant

    def __str__(self):
        return self.question_text

class TestResult(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)  # To‘g‘ri javoblar soni
    total_questions = models.IntegerField(default=0)  # Umumiy savollar soni
    created_at = models.DateTimeField(auto_now_add=True)  # Test qachon yechilgan

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions}"
