from django.db import models
from users.models import CustomUser
# Create your models here.
class HomeWork(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	std = models.CharField(max_length=200)

	homework = models.TextField()

	def __str__(self):
		return "{}: {}".format(self.author, self.name)


class information(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']



class discuss(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, blank=True, null=True)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']