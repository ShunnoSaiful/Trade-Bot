from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Section(models.Model):
	question_section = models.CharField(max_length=250)
	fontawesome      = models.CharField(max_length=50, blank=True)
	svg_image        = models.FileField(upload_to='uploads/', blank=True)

	def __str__(self):
		return str(self.question_section)

class Question(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	question = models.CharField(max_length=500)

	def __str__(self):
		return str(self.question)


class Answer(models.Model):
	question = models.OneToOneField(Question, on_delete=models.CASCADE)
	answer = RichTextUploadingField()


	def __str__(self):
		return str(self.question)

class Plan(models.Model):
	title = models.CharField(max_length=250)
	price = models.IntegerField()
	per_price = models.CharField(max_length=50, default=0)
	first_info = models.CharField(max_length=120, blank=True)
	second_info = models.CharField(max_length=120, blank=True)
	third_info = models.CharField(max_length=120, blank=True)
	fourth_info = models.CharField(max_length=120, blank=True)
	fifth_info = models.CharField(max_length=120, blank=True)

	def __str__(self):
		return self.title



class FeatureCategory(models.Model):
	category = models.CharField(max_length=250, blank=True)


	def __str__(self):
		return str(self.category)

class Description(models.Model):
	category = models.ForeignKey(FeatureCategory, on_delete=models.CASCADE)
	sub_category = models.CharField(max_length=250, blank=True)
	content = RichTextUploadingField()


	def __str__(self):
		return str(self.category)

class Download(models.Model):
	download_file = models.FileField(upload_to='uploads/')


	def __str__(self):
		return str(self.download_file)