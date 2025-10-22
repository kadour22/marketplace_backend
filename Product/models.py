from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=255)              
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)           
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField(default=0)           
    image = models.ImageField(upload_to='products/')        
    
    # Seller info
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    
    # AI-related fields
    ai_generated = models.BooleanField(default=False)        # Whether the description/title was AI-generated
    embedding = ArrayField(models.FloatField(), null=True, blank=True)  # Semantic search embedding vector
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title