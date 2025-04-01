from django.db import models

# Create your models here.
'''
class GetClass(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()

    def __str__(self):
        return self.name
'''

class Subject(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    get_subject_id = models.IntegerField()

    def __str__(self):
        return self.name
    
class Note(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    get_topic_id = models.IntegerField()

    def __str__(self):
        return self.name