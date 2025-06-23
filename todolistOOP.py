class NoTaskAvailability(Exception):
    def __init__(self,message):
        super().__init__(message)
class Task:
    def __init__(self,title):
        self.title=title
        self.completed=False
    def mark_complete(self):
        self.completed=True
    def __str__(self):
        status="Done" if self.completed else "Not Done"
        return f"{self.title}-{status}"
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self,title):
        task=Task(title)
        self.tasks.append(task)
    def remove_task(self,title):
        self.tasks=[task for task in self.tasks if task.title!=title]
    def mark_task_complete(self,title):
        for task in self.tasks:
            if task.title==title:
                task.mark_complete()           
    def show_task(self):
        if not self.tasks:
            raise NoTaskAvailability("No task is available")
        else:
            for task in self.tasks:
                print(task)
todolist=ToDoList()
todolist.add_task("Buy groceries")
todolist.add_task("Complete Python project")
todolist.add_task("Read a book")
print("All Tasks:")
todolist.show_task()
todolist.mark_task_complete("Complete Python project")
print("\nTasks after marking 'Complete Python project' as done:")
todolist.show_task()
todolist.remove_task("Buy groceries")
print("\nTasks after removing 'Buy groceries':")
todolist.show_task()