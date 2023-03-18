from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile # Import profile as defined in Models

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)    # Create user and useradmin 
admin.site.unregister(Group)            # Unregister groups

# Remove: admin.site.register(Profile)
