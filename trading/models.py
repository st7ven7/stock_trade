from django.db import models 
from django.contrib.auth.models import User


#Userprofile to distinguish betn normal user and company user 

class UserProfile(models.Model):
    Normal_user = 'Normal'
    Company_user = 'Company'

    User_Types = [
        (Normal_user, 'Normal User'),
        (Company_user, 'Company User'),
    ]

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    user_type = models.CharField(max_length=7, choices=User_Types, default = Normal_user)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"
    

#creation of compnay

class Company(models.Model):

    company = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'Company'})
    name = models.CharField(max_length=255, unique = True)
    description = models.TextField()

    def __str__(self):
        return self.name 
    
#creation of share which can only be done by company users 

class Share(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_shares = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.company.name} - {self.price}"
    
#transaction model (User can buy or sell shares)

class Transaction(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    Transaction_type = [
        (BUY, 'BUY'),
        (SELL, 'SELL'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    transaction_method = models.CharField(max_length=4, choices=Transaction_type)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.transaction_method} {self.quantity} shares of {self.share.company.name}"