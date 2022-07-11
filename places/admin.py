from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["preview"]
    fields = ["picture", "preview", "order"]
    ordering = ["order"]
    extra = 5

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: {};"/>',
                           mark_safe(obj.picture.url),
                           "200px",
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    ordering = ["pk"]
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
