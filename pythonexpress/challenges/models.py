from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sample(models.Model):
    input_data = models.TextField()
    input_data_type = models.CharField(max_length=20)  # Add data type field for input data
    output_data = models.TextField()
    output_data_type = models.CharField(max_length=20)  # Add data type field for output data

    def __str__(self):
        return f'Sample for Challenge: {self.input_data}'


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    code_template = models.TextField()  # Initial code template for participants
    difficulty = models.CharField(max_length=20)  # You can define difficulty levels (easy, medium, hard)
    date = models.DateField(auto_now_add=False)
    score = models.IntegerField(default=25)
    sample = models.ManyToManyField(Sample, related_name='challenge')


    def __str__(self):
        return self.title



class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    code_solution = models.TextField()
    score = models.IntegerField(default=0)
    negative_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"
