from django.db import models
class Employee(models.Model):
    eid = models.PositiveIntegerField(unique=True)
    ename = models.CharField(max_length=100 )
    eemail = models.EmailField(unique=True)
    econtact = models.PositiveIntegerField( unique=True)
    profile_image = models.FileField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.ename




