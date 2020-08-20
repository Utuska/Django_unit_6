from django.contrib import admin

from .models import Car, Review


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'review_count']
    list_filter = ('brand', 'model')
    search_fields = ['brand', 'model']




class ReviewAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    list_filter = ('car', 'title')
    search_fields = ['car', 'title', 'text']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
