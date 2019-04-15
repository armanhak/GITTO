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
		
class date_answers(models.Model):
	date_value = models.DateField()
	question = models.ForeignKey(questions, on_delete=models.CASCADE)
	class Meta:
		db_table = 'date_answers'

class surveys(models.Model):
	survey_id = models.IntegerField()
	question = models.ForeignKey(questions, on_delete=models.CASCADE)
	option = models.ForeignKey(options_selection, null=True, blank=True, on_delete=models.CASCADE)
	date_answer = models.ForeignKey(date_answers, null=True, blank=True, on_delete=models.CASCADE)
	@property
	def answer_fill(self):
		if self.answer_sel_id is not None:
			answer = self.answer_sel_id
		if self.date_answer is not None:
			answer = self.date_answer
	@property
	def answer_id(self):
		if self.answer_sel_id is not None:
			return self.answer_sel_id
		if self.date_answer is not None:
			return self.date_answer
		# raise AssertionError(«Neither ‘answer_sel_id’ nor date_answer is set»)
	

	class Meta:
		db_table = 'survey'

class raw_text_answer(models.Model):
	answer_text = models.TextField()
	class Meta: 
		db_table = 'raw_text_answer'


  
 


 