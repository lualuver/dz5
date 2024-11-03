class Task:
    def __init__(self, name, description, deadline, is_complete=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_complete = is_complete


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def delete_task(self, task_name):
        for task in self.task_list:
            if task_name == task.name:
                self.task_list.remove(task)

    def mark_complete(self, task_name):
        for task in self.task_list:
            if task_name == task.name:
                task.is_complete = True

    def print_task_list(self):
        for task in self.task_list:
            print("имя: "+task.name+" описание:"+task.description+" дэдлайн: "+task.deadline+" выполнено ли?: "+str(task.is_complete))



task1 = Task( "howme work", "math", "today")
task2 =  Task( "shag", "python", "today")

tm=TaskManager()

tm.add_task(task1)
tm.add_task(task2)
tm.add_task(Task( "shag2", "python2", "tomorow"))
tm.print_task_list()
tm.delete_task("shag")
tm.print_task_list()

