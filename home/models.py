from django.contrib.auth.models import AbstractUser, User, UserManager
from django.db import models

SEX_ITEMS = [
    ("f", "男"),
    ("m", "女"),
    ("n", "未知")
]
# 表示是否离职或者出院
ACTIVE_ITEMS = [
    ("y", "有效"),
    ("n", "无效")
]
# 表示是否移除信息
REMOVE_ITEMS = [
    ("y", "移除"),
    ("n", "未移除")
]


# Create your models here.
class OldPerson(models.Model):
    username = models.CharField(max_length=50, verbose_name="老人姓名")
    gender = models.CharField(max_length=5, verbose_name="老人性别", choices=SEX_ITEMS, default="n")
    phone = models.CharField(max_length=50, verbose_name="老人联系电话", null=True, blank=True)
    id_card = models.CharField(max_length=50, verbose_name="老人身份证号")
    birthday = models.DateField(default="1950-01-01", verbose_name="老人生日", null=True, blank=True)
    checkin_date = models.DateTimeField(verbose_name="入养老院日期", null=True, blank=True)
    checkout_date = models.DateTimeField(verbose_name="出养老院日期", null=True, blank=True)
    profile_photo = models.ImageField('老人人脸信息', upload_to='photo/user', default='', null=True, blank=True)
    # imgset_dir = models.CharField(max_length=200)
    # profile_photo = models.CharField(max_length=200)
    room_number = models.CharField(max_length=50, verbose_name="房间号", null=True, blank=True)

    firstguardian_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="第一监护人姓名")
    firstguardian_relationship = models.CharField(max_length=50, verbose_name="与第一监护人关系", null=True, blank=True)
    firstguardian_phone = models.CharField(max_length=50, verbose_name="第一监护人手机号", null=True, blank=True)
    firstguardian_wechat = models.CharField(max_length=50, verbose_name="第一监护人微信", null=True, blank=True)

    secondguardian_name = models.CharField(max_length=50, verbose_name="第二监护人姓名", null=True, blank=True)
    secondguardian_relationship = models.CharField(max_length=50, verbose_name="与第二监护人关系", null=True, blank=True)
    secondguardian_phone = models.CharField(max_length=50, verbose_name="第二监护人手机号", null=True, blank=True)
    secondguardian_wechat = models.CharField(max_length=50, verbose_name="第二监护人微信", null=True, blank=True)

    health_state = models.CharField(max_length=50, verbose_name="老人健康状态", null=True, blank=True)
    description = models.CharField(max_length=50, verbose_name="描述", null=True, blank=True)
    isactive = models.CharField(max_length=1, verbose_name="是否有效", default="y", choices=SEX_ITEMS)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    createby = models.IntegerField(verbose_name="创建人", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间", null=True, blank=True)
    updateby = models.IntegerField(verbose_name="更新人", null=True, blank=True)
    remove = models.CharField(max_length=1, choices=REMOVE_ITEMS, default="n")

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<OldAge: {}>'.format(self.username)

    class Meta:
        db_table = "oldperson_info"
        verbose_name_plural = "老人信息"


class Employee(models.Model):
    username = models.CharField(max_length=50, verbose_name="职工姓名")
    gender = models.CharField(max_length=5, choices=SEX_ITEMS, verbose_name="职工性别", default="n")
    phone = models.CharField(max_length=50, verbose_name="职工电话")
    id_card = models.CharField(max_length=50, verbose_name="职工身份证号")
    birthday = models.DateField(default="1950-01-01", verbose_name="职工生日")
    hire_date = models.DateTimeField(verbose_name="入职时间", null=True)
    resigh_date = models.DateTimeField(verbose_name="离职时间", null=True)
    profile_photo = models.ImageField('职工头像', upload_to='photo/employee', default='')

    description = models.CharField("描述", max_length=50, null=True)
    isactive = models.CharField("是否有效", max_length=10, choices=ACTIVE_ITEMS, default="y")
    created = models.DateTimeField("创建时间", auto_now_add=True)
    createby = models.IntegerField("创建人", null=True)
    updated = models.DateTimeField("更新时间", auto_now=True, null=True)
    updateby = models.IntegerField("更新人", null=True)
    remove = models.CharField("移除标志", max_length=1, choices=REMOVE_ITEMS)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Employee: {}>'.format(self.username)

    class Meta:
        db_table = "employee_info"
        verbose_name_plural = "职工信息"


class Volunteer(models.Model):
    name = models.CharField("义工姓名", max_length=50)
    gender = models.CharField("性别", max_length=5, choices=SEX_ITEMS, default="n")
    phone = models.CharField("联系电话", max_length=50)
    id_card = models.CharField("身份证号", max_length=50)
    birthday = models.DateField(default="1950-01-01", verbose_name="义工生日", null=True)
    checkin_data = models.DateTimeField(verbose_name="访问日期", null=True)
    checkout_data = models.DateTimeField(verbose_name="离开日期", null=True)
    profile_photo = models.ImageField('义工头像', upload_to='photo/volunteer', default='')

    description = models.CharField("描述", max_length=50, null=True)
    isactive = models.CharField("是否有效", max_length=10, choices=ACTIVE_ITEMS, default="y")
    created = models.DateTimeField("创建时间", auto_now_add=True)
    createby = models.IntegerField("创建人", null=True)
    updated = models.DateTimeField("更新时间", auto_now=True, null=True)
    updateby = models.IntegerField("更新人", null=True)
    remove = models.CharField("移除标志", max_length=1, choices=REMOVE_ITEMS)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Volunteer: {}>'.format(self.name)

    class Meta:
        db_table = "volunteer_info"
        verbose_name_plural = "义工信息"


class Event(models.Model):
    EVENT_ITEMS = [
        (0, "情感检测"),
        (1, "义工交互检测"),
        (2, "陌生人检测"),
        (3, "摔倒检测"),
        (4, "禁止区域入侵检测"),
    ]
    event_type = models.IntegerField(choices=EVENT_ITEMS)
    event_date = models.DateTimeField(auto_now_add=True)
    event_location = models.CharField(max_length=200, null=True)
    event_desc = models.CharField(max_length=200, null=True)
    oldperson = models.ForeignKey(OldPerson, on_delete=models.DO_NOTHING)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Event: {}>'.format(self.oldperson, self.event_desc)

    class Meta:
        db_table = "event_info"
        verbose_name_plural = "事件检测"


class OldPersonManager(UserManager):

    def create_user(self, email=None, password=None, **extra_fields):
        real_name = extra_fields.get("real_name")
        super().create_user(username=real_name, password=password, email=email, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        real_name = extra_fields.get("real_name")
        super().create_superuser(username=real_name, password=password, email=email, **extra_fields)


class SystemUser(AbstractUser):
    # 用于权限认证的user一对一关联
    # auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField("用户名", max_length=50)
    # password = models.CharField("密码", max_length=50)
    real_name = models.CharField("管理员真实姓名", max_length=50)
    gender = models.CharField("性别", max_length=5, choices=SEX_ITEMS, default="n")
    email = models.CharField("注册邮箱", max_length=50, unique=True)
    phone = models.CharField("手机号码", max_length=50)

    description = models.CharField("描述", max_length=50, null=True)
    isactive = models.CharField("是否有效", max_length=10, choices=ACTIVE_ITEMS, default="y")
    created = models.DateTimeField("创建时间", auto_now_add=True)
    createby = models.IntegerField("创建人", null=True)
    updated = models.DateTimeField("更新时间", auto_now=True, null=True)
    updateby = models.IntegerField("更新人", null=True)
    remove = models.CharField("移除标志", max_length=1, choices=REMOVE_ITEMS)

    datafilter = models.CharField("数据过滤", max_length=200, null=True)
    theme = models.CharField("主题", max_length=45, null=True)
    defaultpage = models.CharField("缺省页面", max_length=45, null=True)
    logoimage = models.CharField("Logo", max_length=45, null=True)
    appversion = models.CharField("app版本", max_length=10, null=True)
    jsonauth = models.CharField("app版本控制，json串中的权限点配置", max_length=1000, null=True)

    USERNAME_FIELD = 'email'
    objects = OldPersonManager()

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    # @property
    # def is_authenticated(self):
    #     """
    #     Always return True. This is a way to tell if the user has been
    #     authenticated in templates.
    #     """
    #     return True

    def __str__(self):
        return '<SystemUser: {}>'.format(self.username)

    class Meta:
        db_table = "system_user"
        verbose_name_plural = "系统用户信息"

    REQUIRED_FIELDS = ['real_name']

