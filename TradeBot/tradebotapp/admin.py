from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Plan, Description, Download, Section, FeatureCategory


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Plan)
admin.site.register(Description)
admin.site.register(Download)
admin.site.register(FeatureCategory)
admin.site.register(Section)


