from django.db import models

# Create your models here.
#!/usr/bin/env python3

class Customer(models.Model):
    name = models.TextField()
    userID = models.TextField()
    Designation = models.TextField()
    description = models.TextField(default = 'I AM A HACKER BUT HONEST')
