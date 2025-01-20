# Code 2: Simple To-Do List

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task): 
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        return f"Task '{task}' not found."

    def view_tasks(self):
        return "\n".join(self.tasks) if self.tasks else "No tasks available."

if __name__ == "__main__":
     # Test Todo List
    todo = TodoList()
    print(todo.add_task("Complete Python Project"))
    print(todo.view_tasks())
