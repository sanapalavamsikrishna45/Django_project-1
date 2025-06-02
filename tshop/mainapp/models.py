from django.db import models

# Create your models here.


class Product(models.Model):
   # this class during migration, leads to cretion of a new table called mainapp_product.
   # In django, by default, every created table follows the naming pattern <app_name>_<modelname>
    
    # A primary key column called id is autometically present for every model in django
    # Hence, We don't need to create an id column
    # Rest of the column we create in the following fashion 
    
    name = models.CharField(max_length=200) # this creates a VARCHAR(200) cloumn
    price = models.PositiveIntegerField() # This created an INT column and checks for postitive value
    stock = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/',  null=True) # This stores the image into 'products' subfolder
                                                     # in the 'MEDIA_URL'
                                                     # The file path of the stored image will be stored in this column
                                                     # as VARCHAR in the db
    
    
    # overriding the __str__ method  //no need to migrate after righting code by using python...
    def __str__(self):
        return f"Product > {self.name}"
    
                                                     
    