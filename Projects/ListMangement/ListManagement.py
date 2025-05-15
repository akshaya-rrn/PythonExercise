# for only one user
# Add, Modify, Delete actionitems in list
# Get Lists
# Action Item - Complete, Not 

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    # ~ Object.ToString() in Java
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.name} [{status}]"
        

class TaskManagement:
    
    def __init__(self):
        self.tasks = []
     
    def get_tasks(self):
        return self.tasks

    def add_task(self, name):
        self.tasks.append(Task(name))
        
    def delete_task(self, name):
        for task in self.tasks:
            if(task.name == name):
                self.tasks.remove(task)
                return True
            
        return False

    def edit_task(self, name, updatedTaskName):
        for task in self.tasks:
            if(task.name == name):
                task.name = updatedTaskName
                return True
            
        return False
    
        

    def mark_task_complete(self, name):
        for task in self.tasks:
            if(task.name == name):
                task.completed = True
                return True
               
        return False



def main():
    task_manager = TaskManagement()
    tasks = task_manager.get_tasks()

    for i in range(10):
        task_manager.add_task(f"Add Task Number : {i+1}")

    for i in [5,6,7]:
        task_manager.mark_task_complete(f"Add Task Number : {i}")
    

    tasks = task_manager.get_tasks()
    
    for task in tasks:
       print(task)
    
    print(" Deleting the task: 2,3,4 now .......  and list the tasks")
    
    for i in [2,3,4]:
        task_manager.delete_task(f"Add Task Number : {i}")
   

    for task in task_manager.get_tasks():
        print(task)
    


if __name__ == "__main__":
    main()
    




    