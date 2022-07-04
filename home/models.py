from django.db import models


# Create your models here.
class OldPerson(models.Model):
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    checkin_data = models.DateTimeField()
    checkout_data = models.DateTimeField()
    profile_photo = models.ImageField('用户头像', upload_to='photo/user', default='')
    # imgset_dir = models.CharField(max_length=200)
    # profile_photo = models.CharField(max_length=200)
    room_number = models.CharField(max_length=50)

    firstguardian_name = models.CharField(max_length=50)
    firstguardian_relationship = models.CharField(max_length=50)
    firstguardian_phone = models.CharField(max_length=50)
    firstguardian_wechat = models.CharField(max_length=50)

    secondguardian_name = models.CharField(max_length=50)
    secondguardian_relationship = models.CharField(max_length=50)
    secondguardian_phone = models.CharField(max_length=50)
    secondguardian_wechat = models.CharField(max_length=50)

    health_state = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    isactive = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    createby = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    updateby = models.IntegerField()
    remove = models.CharField(max_length=1)

    class Meta:
        db_table = "oldperson_info"


class Employee(models.Model):
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    hire_date =models.DateTimeField()
    resigh_date = models.DateTimeField()
    profile_photo = models.ImageField('职工头像', upload_to='photo/employee', default='')

    description = models.CharField(max_length=50)
    isactive = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    createby = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    updateby = models.IntegerField()
    remove = models.CharField(max_length=1)

    class Meta:
        db_table = "employee_info"


class Volunteer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    checkin_data = models.DateTimeField()
    checkout_data = models.DateTimeField()
    profile_photo = models.ImageField('义工头像', upload_to='photo/volunteer', default='')

    description = models.CharField(max_length=50)
    isactive = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    createby = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    updateby = models.IntegerField()
    remove = models.CharField(max_length=1)

    class Meta:
        db_table = "volunteer_info"


class Event(models.Model):
    event_type = models.IntegerField("事件类型：0表示情感检测，，1代表义工交互检测，2代表陌生人检测，3代表摔倒检测，4代表禁止区域入侵检测")
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=200)
    event_desc = models.CharField(max_length=200)
    oldperson = models.ForeignKey(OldPerson, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "event_info"


class SystemUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    isactive = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    createby = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    updateby = models.IntegerField()
    remove = models.CharField(max_length=1)
    datafilter = models.CharField(max_length=200)
    theme = models.CharField(max_length=45)
    defaultpage = models.CharField(max_length=45)
    logoimage = models.CharField(max_length=45)
    appversion = models.CharField(max_length=10)
    jsonauth = models.CharField("app版本控制，json串中的权限点配置", max_length=1000)
