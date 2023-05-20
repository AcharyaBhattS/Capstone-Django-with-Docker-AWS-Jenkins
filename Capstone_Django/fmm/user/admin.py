from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from fmm.user.forms import UserChangeForm, UserCreationForm

from fmm.user.models import (User, UserSocialInfo, UserPersonalInfo,
                             UserEducation, UserExpertise, UserMentorAccount,
                             UserYuweeAccount, UserMentorSchedule)

from .forms import YuweeRegisterForm


def request_password_resets(modeladmin, request, queryset):
    for user in queryset:
        user.request_password_reset(initial=False)


def apply_mentors_for_approval(modeladmin, request, queryset):
    for mentor in queryset:
        mentor.apply_for_approval()


def approve_mentor_applications(modeladmin, request, queryset):
    for mentor in queryset:
        mentor.approve()


def reject_mentor_applications(modeladmin, request, queryset):
    for mentor in queryset:
        mentor.reject()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = auth_admin.UserAdmin.fieldsets + ((None, {'fields': ('avatar',)}),)
    list_display = ["id", "username", "is_superuser"]
    search_fields = ["username"]
    readonly_fields = ["id"]
    actions = [request_password_resets, ]


@admin.register(UserPersonalInfo)
class UserPersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'yuwee_flag']
    form = YuweeRegisterForm


@admin.register(UserSocialInfo)
class UserSocialInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(UserEducation)
class UserEducationAdmin(admin.ModelAdmin):
    pass


@admin.register(UserExpertise)
class UserExpertiseAdmin(admin.ModelAdmin):
    pass


@admin.register(UserYuweeAccount)
class UserYuweeAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_display_links = ('user',)
    ordering = ('id',)


@admin.register(UserMentorAccount)
class UserMentorAccountAdmin(admin.ModelAdmin):
    actions = [apply_mentors_for_approval, approve_mentor_applications,
               reject_mentor_applications, ]
    list_display = ['user', 'can_create_free_workshops', 'top']
    list_editable = ['can_create_free_workshops', 'top']


@admin.register(UserMentorSchedule)
class UserMentorScheduleAdmin(admin.ModelAdmin):
    pass
