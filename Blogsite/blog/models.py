from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    mnumber = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.CharField(max_length=50)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + "Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('add_blogs')

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "Comment: " + self.content

    


