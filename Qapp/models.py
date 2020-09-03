from django.db import models
from PIL import Image
from django.shortcuts import render

class accounts(models.Model):
    name=models.CharField(max_length=40,null=False)
    username=models.CharField(max_length=40,unique=True,null=False)
    password=models.CharField(max_length=40,null=False)
    acc_type=models.CharField(max_length=40,null=False)

    def __str__(self):
        return "name : "+self.name+", username : "+self.username+", password : "+self.password+", acc_type : "+self.acc_type+"\n"
    
    def acc_color(self):
        acc_color_dict= {
            'basic':'black',
            'requested':'black',
            'teacher':'red',
            'premium':'gold'
        }
        return str(acc_color_dict[self.acc_type])


class question(models.Model):
    Qtitle=models.CharField(max_length=100,null=True)
    Qdesc=models.CharField(max_length=300,null=True)
    img1=models.ImageField(upload_to="images/",null=True,blank=True)
    img2=models.ImageField(upload_to="images/",blank=True)
    img3=models.ImageField(upload_to="images/",blank=True)
    img4=models.ImageField(upload_to="images/",blank=True)
    asked_by=models.ForeignKey(accounts,on_delete=models.CASCADE,blank=True,null=True)


#--------------------------------------------------
    def asker(self):
        return self.asked_by.username

    def get_img1(self):
        try:
            return str(self.img1.url)
        except:
            return ""
    def is_img1(self):
        try:
            a=self.img1.url
            return True
        except:
            return False

    def get_img2(self):
        try:
            return str(self.img2.url)
        except:
            return ""
    def is_img2(self):
        try:
            a=self.img2.url
            return True
        except:
            return False
    def get_img3(self):
        try:
            return str(self.img3.url)
        except:
            return ""
    def is_img3(self):
        try:
            a=self.img3.url
            return True
        except:
            return False
    def get_img4(self):
        try:
            return str(self.img4.url)
        except:
            return ""
    def is_img4(self):
        try:
            a=self.img4.url
            return True
        except:
            return False
#----------------------------------------------
    def __str__(self):
        try:
           desc=self.Qdesc
        except:
           desc=""
    #    try:
    #        asker=self.asked_by.username
    #    except:
    #        asker=""
        return "title : "+self.Qtitle+", description : "+desc+", asked_by : "+self.asker()+"\n"


class answer(models.Model):
    Adesc=models.CharField(max_length=500)
    img1=models.ImageField(upload_to="images/",null=True,blank=True)
    img2=models.ImageField(upload_to="images/",null=True,blank=True)
    img3=models.ImageField(upload_to="images/",null=True,blank=True)
    img4=models.ImageField(upload_to="images/",null=True,blank=True)
    ques=models.ForeignKey(question,on_delete=models.CASCADE,null=True,blank=True)
    answered_by=models.ForeignKey(accounts,on_delete=models.CASCADE,null=True,blank=True)

    def answerer(self):
        return self.answered_by.username
    
    def __str__(self):
        return 'Question:'+self.ques.Qtitle+' , answer:'+self.Adesc+' , By:'+self.answered_by.username+'\n'

