from django.db import models

# Create your models here.
class Task(models.Model):
    Task_Name = models.CharField('Task Name', max_length = 120)
    Due_Date = models.DateField("Due_Date")
    Status = models.BooleanField("Status",default=False, choices=[(True, 'Completed'), (False, 'Not completed')])
    Description = models.TextField("Description", blank = True, max_length=300)
    

    def __str__(self):
        return self.Task_Name 