from django.contrib import admin
from .models import TourCategory,Municipality,AvailableDate,Tour,Deparment

# Register your models here.
class TourCategoryAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class TourAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")


admin.site.register(TourCategory, TourCategoryAdmin)

admin.site.register(Tour,TourAdmin)

admin.site.register(AvailableDate)

admin.site.register(Municipality)

admin.site.register(Deparment)