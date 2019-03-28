from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
  		return self.user.username
class questions(models.Model):	 
	question_name = models.CharField(max_length = 60)
	question_type = models.CharField(max_length = 25)
	class Meta:
		verbose_name = 'Вопросы'
		db_table = 'questions'

class options_selection(models.Model):	
	question = models.ForeignKey(questions, on_delete=models.CASCADE)
	option_id = models.IntegerField()
	option_name = models.TextField()
	class Meta:
		db_table = 'options_selection'
		unique_together = (('question', 'option_id'),)
class surveys(models.Model):
	question = models.ForeignKey(questions, on_delete=models.CASCADE)
	question_answer = models.IntegerField()
	class Meta:
		db_table = 'surveys'
class raw_text_answer(models.Model):
	answer_text = models.TextField()
	class Meta: 
		db_table = 'raw_text_answer'
class date_answers(models.Model):
	date_value = models.DateField()
	class Meta:
		db_table = 'date_answers'
	