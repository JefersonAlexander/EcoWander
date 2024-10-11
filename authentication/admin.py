from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('first_name', 'last_name','email', 'type_document', 'number_document', 'phone')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ('first_name', 'last_name','email', 'type_document', 'number_document', 'phone')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserProfile
    list_display = ('email','first_name', 'last_name', 'type_document', 'number_document', 'phone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'type_document', 'number_document', 'phone')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'type_document', 'number_document', 'phone')}
        ),
    )
    search_fields = ('email','first_name', 'last_name', 'number_document')
    ordering = ('email',)


admin.site.register(UserProfile, CustomUserAdmin)