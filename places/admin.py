from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ["picture", "preview", "order"]
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: {};"/>',
                           mark_safe(obj.picture.url),
                           "200px",
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ["pk"]



