# portfolio/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Portfolio, Project

class PortfolioInline(admin.StackedInline):
    model = Portfolio
    can_delete = False
    verbose_name_plural = 'Portfolios'
    filter_horizontal = ('projects',)

class CustomUserAdmin(UserAdmin):
    inlines = (PortfolioInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project)