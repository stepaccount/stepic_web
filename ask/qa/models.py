from django.db import models
from django.contrib.auth.models import User

#Question manager
class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass

#Question model
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name = '+')
    likes = models.ManyToManyField(User, related_name = '+')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        ordering = ['-added_at']
        pass

#Answer model
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, related_name = '+')
    def __unicode__(self):
        return self.title
    class Meta:
        pass

