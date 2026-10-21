from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.TextField()
    location = models.CharField()
    description = models.TextField()
    salary = models.IntegerField()
    created_at = models.DateField(auto_now_add=True) 
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
   
    def __str__(self):
            return self.title
    

