from django.contrib import admin
from .models import Player, Favorite, Contact



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "country",
        "role",
        "featured",
        "featured_order",
    )
    
    list_editable = (
    "featured",
    "featured_order",
    )
    
    search_fields = (
    "name",
    "country",
    )

    list_filter = (
        "country",
        "role",
    )

    ordering = (
        "name",
    )
    
admin.site.register(Favorite)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )
    
admin.site.site_header = "CricPedia Administration"

admin.site.site_title = "CricPedia Admin"

admin.site.index_title = "Welcome to CricPedia Dashboard"