tasks=[]
task_id_counter=1
#we need to give each task a unique id
def add_task():
    
    global task_id_counter
    description = input("enter task description :")
    task = {"id": task_id_counter, "description": description, "status": "pending" }
    tasks.append(task)
    print(f"Task added with id{task_id_counter}!")
    task_id_counter += 1

def view_tasks():
    if not tasks:
        print("no tasks yet!")
        return
    print("\n your tasks:")
    for task in tasks:
        print(f"ID{task['id']} | Description: {task['description']} | Status: {task['status']}")   
    print()
    
def update_task(): 
    view_tasks()
    try:
        task_id=int(input("Enter task id to mark as done"))
        for task in tasks:
            if task["id"]==task_id:
               task["status"]= "done"
               print(f"Task {task_id} marked as done!")
               return
        print("task id not found")
    except ValueError:
        print("please enetr a valid number!")


def delete_task():
    view_tasks()
    try:
        task_id=int(input("Enter task id to delete:"))
        for i, task in enumerate(tasks):
            if task["id"]==task_id:
                del tasks[i]
                print(f"Task{task_id} deleted")
                return
        print("task id not found")
    except ValueError:
            print("pleae enter a valid number")

    #main loop started
while True:
    print("\n to do list menu")
    print("1.add task")
    print("2.view task")
    print("3.update task")
    print("4.delete task")
    print("5.quit")

    choice=input("choose an option(1_5):")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        update_task()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        print("goodbye!")
        break

    else:
         print("invalid choice try again!")     
 
