import logging

from django.contrib import admin
from django.utils.html import format_html

from .models import AllureResult, AllureReport

logger = logging.getLogger(__name__)


def delete_object(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()


@admin.register(AllureResult)
class AllureResultAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date')
    list_display = ('id', 'path')
    actions = [delete_object]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(AllureReport)
class AllureReportAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date', 'path')
    list_display = ('id', 'result_id', 'service_name', 'env', 'path_link')
    list_filter = ['service_name', 'env']
    actions = [delete_object]

    def path_link(self, instance):
        return format_html(f"<a href='{instance.path}'>View report</a>")

    path_link.short_description = 'Report url'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
