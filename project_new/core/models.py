from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128) 
    is_active = models.BooleanField(default=True)
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    Category = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Home Appliances', 'Home Appliances'),
        ('Books', 'Books'),
        ('Sports', 'Sports'),
    )


    name = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50, choices=Category, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    def edit(self, name, price, category, description, image):
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        if image:
            self.image = image
        self.save()


class Event(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


    def __str__(self):
        return self.title
    

    def edit(self, title, description, start_date, end_date, location):
        if end_date and start_date and end_date < start_date:
            raise ValueError("End date must be after start date")
        
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.save()    
    



