from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=100,help_text="enter author name")


    def __str__(self):
        return self.author_name


class Category(models.Model):
    category_name=models.CharField(max_length=100,help_text="enter Book category",verbose_name="Category")
    class Meta:
        verbose_name_plural="category"


    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_name=models.CharField(max_length=100,help_text="enter name of book")
    book_price=models.IntegerField(help_text="enter price of book")
    book_isbn_Num=models.CharField(max_length=100, help_text="enter isbn number")
    author_name=models.ForeignKey(Author,on_delete = models.CASCADE)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.book_name



class Member(models.Model):
     member_name=models.CharField(max_length=100,help_text="enter name of member")
     member_last_name=models.CharField(max_length=100,help_text="enter last name of member")
     member_phone_number=models.IntegerField(help_text="enter phone number of a  member")
     member_email=models.EmailField(help_text="enter email  of member")

     def __str__(self):
         return self.member_name

class Record(models.Model):
    issue_date=models.DateField()
    return_date=models.DateField()
    book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    member_name=models.ForeignKey(Member,on_delete=models.CASCADE)

def __str__(self):
    return self.issue_date



