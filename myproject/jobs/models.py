from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title