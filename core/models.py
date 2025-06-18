from django.db import models



class CustmerUser(models.Model):
    First_name = models.CharField(max_length=200,blank=True)
    Last_name =models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
    




class Profile(models.Model):
    user= models.OneToOneField(CustmerUser, on_delete=models.CASCADE)
    phone =models.CharField(max_length=20, blank=True)



    



