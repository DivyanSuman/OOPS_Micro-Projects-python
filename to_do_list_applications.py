
import pandas as pd
class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority

class To_Do_List:
    def __init__(self):
        self.tasks = []

    def add_tasks (self, task):
        self.tasks.append(task)

    def del_tasks (self, task_name):
        for task in self.tasks[:]:
            if task.name == task_name:
                self.tasks.remove(task)

    def display_tasks (self):
        tasks = []
        if not self.tasks:
            print('No tasks in To-Do List')
        else:
            for index, value in enumerate(self.tasks, start = 1):
                task ={
                    'index': index,
                    'name': value.name,
                    'Due_date': value.due_date,
                    'Priority': value.priority
                }
                tasks.append(task)
            tasks = pd.DataFrame(tasks)
            print(tasks.to_string(index = False))


# Examples of adding creating task
t1 = Task('Learn English', '05-03-2024', 'Low')
t2 = Task('Learn Python', '20-04-2024', 'High')
t3 = Task('Larn C', '05-06-2024', 'High')
t4 = Task('Learn C++', '20-06-2024', 'High')

# Examples of uses of To_Do_List
to_do = To_Do_List()
to_do.add_tasks(t1)
to_do.add_tasks(t2)
to_do.add_tasks(t3)
to_do.add_tasks(t4)
to_do.del_tasks('Larn C')
to_do.display_tasks()



