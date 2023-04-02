import logging

from django.contrib import admin
from django.utils.html import format_html

from .models import AllureResult, AllureReport

logger = logging.getLogger(__name__)


@admin.register(AllureResult)
class AllureResultAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date')
    list_display = ('id', 'path')


@admin.register(AllureReport)
class AllureReportAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date')
    list_display = ('id', 'result_id', 'service_name', 'env', 'path_link')

    def path_link(self, instance):
        return format_html(f"<a href='{instance.path}'>{instance.path}</a>")
