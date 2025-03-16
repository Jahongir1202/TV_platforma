from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Users, Ertaklar, WatchedVideo, Multfilmlar, WatchedMultfilm, \
    Qoshiqlar, WatchedQoshiqlar, Qiziqari_Matematika, WatchedMatematika, \
    Ingliztili, WatchedIngliztili, Badantarbiya, WatchedBadantarbiya, \
    Rasmlar, WatchedRasmlar, Ariza, TestQuestion, TestResult

# 📌 Hamma video turlari uchun umumiy kategoriya
VIDEO_CATEGORIES = {
    "ertaklar": (Ertaklar, WatchedVideo),
    "multfilmlar": (Multfilmlar, WatchedMultfilm),
    "qoshiqlar": (Qoshiqlar, WatchedQoshiqlar),
    "matematika": (Qiziqari_Matematika, WatchedMatematika),
    "ingliztili": (Ingliztili, WatchedIngliztili),
    "badantarbiya": (Badantarbiya, WatchedBadantarbiya),
    "rasmlar": (Rasmlar, WatchedRasmlar),
}


# ✅ **Foydalanuvchi admin paneli (ko‘rilgan videolar foizi bilan)**
class UsersAdmin(admin.ModelAdmin):
    list_display = ["username"]

    def _generate_watched_percent(model, watched_model):
        def watched_percent(self, obj):
            total_videos = model.objects.count()
            watched_videos = watched_model.objects.filter(user=obj, watched=True).count()
            if total_videos == 0:
                return "0%"
            percent = (watched_videos / total_videos) * 100
            return f"{percent:.2f}%"

        return watched_percent

    total_fields = []
    for key, (VideoModel, WatchedModel) in VIDEO_CATEGORIES.items():
        func_name = f"watched_{key}_percent"
        locals()[func_name] = _generate_watched_percent(VideoModel, WatchedModel)
        locals()[func_name].short_description = f"{key.capitalize()} (%)"
        list_display.append(func_name)
        total_fields.append(func_name)

    # ✅ **Umumiy ko‘rilgan videolar foizi**
    def total_watched_percent(self, obj):
        total_percent = 0
        category_count = 0

        for key, (VideoModel, WatchedModel) in VIDEO_CATEGORIES.items():
            total_videos = VideoModel.objects.count()
            watched_videos = WatchedModel.objects.filter(user=obj, watched=True).count()

            if total_videos > 0:
                total_percent += (watched_videos / total_videos) * 100
                category_count += 1

        if category_count == 0:
            return "0%"

        return f"{(total_percent / category_count):.2f}%"

    total_watched_percent.short_description = "Umumiy Ko‘rilgan (%)"
    list_display.append("total_watched_percent")


# ✅ **Videolar admin paneli (iframe preview bilan)**
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_preview")

    def video_preview(self, obj):
        """YouTube video previewni admin panelda ko‘rsatish"""
        if obj.embed_video():
            return mark_safe(
                f'<iframe width="200" height="100" src="{obj.embed_video()}" frameborder="0" allowfullscreen></iframe>')
        return "No Video"

    video_preview.short_description = "Video Preview"


# 📌 **Admin panelga hamma modellarni avtomatik ro‘yxatdan o‘tkazamiz**
admin.site.register(Users, UsersAdmin)

for key, (VideoModel, _) in VIDEO_CATEGORIES.items():
    admin.site.register(VideoModel, VideoAdmin)


class ArizaAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "created_at")
    search_fields = ("full_name", "phone_number")
    list_filter = ("created_at",)

class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "correct_option")

class TestResultAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "total_questions", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username",)

admin.site.register(TestQuestion, TestQuestionAdmin)  # ✅ TestQuestion alohida ro‘yxatdan o‘tgan
admin.site.register(TestResult, TestResultAdmin)

admin.site.register(Ariza, ArizaAdmin)