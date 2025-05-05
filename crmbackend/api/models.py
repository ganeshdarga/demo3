from django.db import models
import datetime



class activities(models.Model):
    id = models.AutoField(primary_key=True)
    dates = models.DateField()
    days = models.CharField(max_length=255)
    starttime = models.TimeField()
    endtime = models.TimeField()
    Discription = models.CharField(max_length= 255)

class admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class companies(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    mobile = models.IntegerField()
    manage = models.CharField(max_length=255)
    statuss = models.CharField(max_length=255)

class invoice(models.Model):
    id = models.AutoField(primary_key=True)
    accountNumber = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    Amount = models.IntegerField()
    invoiceDate = models.CharField(max_length=255)
    dueDate = models.CharField(max_length=255)
    type= models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class leads(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    phone = models.IntegerField()
    email =models.CharField(max_length=255)
    lead_status = models.CharField(max_length=255)
    Lead_created = models.CharField(max_length=255)
    Lead_owner = models.CharField(max_length=255)

class prequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    contactno = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    services  = models.CharField(max_length=255)
    others = models.CharField(max_length=255)
    query = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    posting_date = models.DateField()
    remark = models.BigIntegerField()

class tasks(models.Model):
    id = models.AutoField(primary_key=True)
    Taskname = models.CharField(max_length=255)
    deadLine = models.DateField(max_length=255)
    status =models.CharField(max_length=255)
    Asignee =models.CharField(max_length=255)

class ticket(models.Model):
    id = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    task_type = models.CharField(max_length=255)
    prioprity =models.CharField(max_length=255)
    ticket = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    admin_remark = models.CharField(max_length=255)
    posting_date = models.DateField()
    admin_remark_date = models.DateTimeField(default=datetime.datetime.now)  # Change here

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    alt_email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address =models.CharField(max_length=255)
    status = models.IntegerField()
    posting_date = models.TimeField()

class usercheck(models.Model):
    id = models.AutoField(primary_key=True)
    logindate = models.CharField(max_length=255)
    logintime = models.CharField(max_length=255)
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    mac = models.BinaryField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class usernotification(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    status = models.IntegerField()
    statusdata = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)

















    




