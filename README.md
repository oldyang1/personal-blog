### 项目启动：
cd myblog

python manage.py runserver

setting中的SECRET_KEY 自行配置

### 后台管理员账号密码修改
进入shell环境，

python3 manage.py shell

执行：

from django.contrib.auth.models import User

u = User.objects.get(username='一个叶小小')

u.set_password('新密码')

u.save()

再进入后台修改用户名即可
