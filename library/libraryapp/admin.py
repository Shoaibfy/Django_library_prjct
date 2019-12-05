from django.contrib import admin
from libraryapp.models import *
from django import forms
# Register your models here.




class AuthorAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(AuthorAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        author=self.cleaned_data.get("author_name")
        if len(author)<3:
            raise forms.ValidationError("please enter name greater than 4 char",code="invalid")
        return self.cleaned_data

    def save(self,commit=True):
        return super(AuthorAdminForm,self).save(commit=commit)

class AuthorAdmin(admin.ModelAdmin):
    search_fields=("author_name",)
    ordering=("author_name",)
    form=AuthorAdminForm

class BookAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        book=self.cleaned_data.get("book_name")
        if len(book)<3:
            raise forms.ValidationError("please enter name greater than 4 char",code="invalid")
        return self.cleaned_data
    def save(self,commit=True):
        return super(BookAdminForm,self).save(commit=commit)
class BookAdmin(admin.ModelAdmin):
    list_display=("book_name","book_price","author_name","category_name",)
    list_filter=("book_price",)
    search_fields=("book_name",)
    ordering=("book_name",)
    form=BookAdminForm

class MemberAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(MemberAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        member=self.cleaned_data.get("member_phone_number")
        if len(str(member)) !=10:
            raise forms.ValidationError("please enter 10 digits phone number",code="invalid")
        return self.cleaned_data
    def save(self,commit=True):
        return super(MemberAdminForm,self).save(commit=commit)



class MemberAdmin(admin.ModelAdmin):
    list_display=("member_name","member_phone_number","member_email",)
    list_filter=("member_phone_number",)
    search_fields=("member_name",)
    ordering=("member_name",)
    form=MemberAdminForm
class CategoryAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(CategoryAdminForm,self).__init__(*args,**kwargs)
    def clear(self):
        category=self.cleaned_data.get("category_name")
        if len(category)<4:
            raise forms.ValidationError("please enter char greater than 4",code="invalid")
        return self.cleaned_data
    def save(self,commit=True):
        return super(CategoryAdminForm,self).save(commit=commit)

class CategoryAdmin(admin.ModelAdmin):
    form=CategoryAdminForm

admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
# admin.site.register(Record)

    
