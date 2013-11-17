from django.contrib import admin
from Exercise.models import *

class SettingAdmin(admin.ModelAdmin):
    pass

class CodeInline(admin.TabularInline):
    model = Checkpoint_Code

class CheckpointAdmin(admin.ModelAdmin):
    inlines=[CodeInline]
    list_display = ['__unicode__', 'times_claimed', 'grid']


class ActionAdmin(admin.ModelAdmin):
    list_filter = ['section', 'section__platoon']
    list_display = ['section', 'time', 'points']


class SectionInline(admin.TabularInline):
    model = Section


class PlatoonAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ['__unicode__', 'total_points']


admin.site.register(Setting, SettingAdmin)
admin.site.register(Checkpoint, CheckpointAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Platoon, PlatoonAdmin)
