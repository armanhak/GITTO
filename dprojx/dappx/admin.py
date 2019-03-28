from django.contrib import admin
from dappx.models import UserProfileInfo, User, questions, options_selection, surveys,raw_text_answer, date_answers
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(questions)
admin.site.register(options_selection)
admin.site.register(surveys)
admin.site.register(raw_text_answer)
admin.site.register(date_answers)
