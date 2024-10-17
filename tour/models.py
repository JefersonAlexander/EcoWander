from django.db import models

# Create your models here.
class Deparment(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name="deparment"
        verbose_name_plural="deparments"

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name=models.CharField(max_length=50)
   
    class Meta:
        verbose_name="municipality"
        verbose_name_plural="municipaiyties"

    def __str__(self):
        return self.name


class TourCategory(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="tourCategory"
        verbose_name_plural="tourCategories"

    def __str__(self):
        return self.name
    
class AvailableDate(models.Model):
    date = models.DateField(unique=True)

    class Meta:
        verbose_name="availableDate"
        verbose_name_plural="availableDates"
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

class Tour(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    municipality=models.ForeignKey(Municipality, on_delete=models.CASCADE)
    deparment=models.ForeignKey(Deparment, on_delete=models.CASCADE)
    categories=models.ManyToManyField(TourCategory) 
    availableDate=models.ManyToManyField(AvailableDate) 
    price=models.FloatField()
    images=models.ImageField(upload_to="tour", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="tour"
        verbose_name_plural="tours"
    
    def __str__(self):
        return self.name
