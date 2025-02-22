from locust import TaskSet, HttpUser


# 1.定义任务
# 注：普通函数，必须要有一个形参
# 任务1：说话
def say(params):
    print("正在说话")


# 任务2：唱歌
def ring(params):
    print("正在唱歌")


# 2.定义任务集
# 注：一个类必须继承TaskSet，复写tasks--格式为列表或者字典，值为任务函数名
class TaskTest(TaskSet):
    # 复写tasks
    tasks = [say, ring]


# 3.定义用户类
# 注：一个类必须继承HttpLocust，复写task_set参数，值为任务集类名称
class RunUser(HttpUser):
    # 复写task_set
    task_set = TaskTest
