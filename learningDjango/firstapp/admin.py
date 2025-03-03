from django.contrib import admin
from .models import Firstapp, Review, Store, Profile

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2


class FirstappAdmin(admin.ModelAdmin):
    list_display = ('name','superheros','date_added')
    inlines = [ReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('products',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','bio')

admin.site.register(Firstapp, FirstappAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review)
