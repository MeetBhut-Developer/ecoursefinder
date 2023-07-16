from django.db import models

# Create your models here.
class Master_Courses(models.Model):
    course_name=models.TextField(max_length=50)
    img_url=models.TextField()
    course_url=models.TextField()
    university_name=models.TextField(max_length=22)
    course_description=models.CharField(max_length=100)
    rating_count=models.CharField(max_length=10)
    review_count=models.CharField(max_length=50)
    price=models.CharField(max_length=5)
    start_date=models.CharField(max_length=10)

    class Meta:
        db_table='master_courses_table'