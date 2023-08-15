from django.db import models


# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text or "no question"

    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField("time of publication")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
