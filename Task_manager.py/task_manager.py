def task():
    task=[]#empty list
    print("------WEL COME TO THE TASK MANAGER------")

    total_task=int(input("How many task you gonna do today:"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        task.append(task_name)
    
    print(f"todays task are \n {task}")
    

    while True:
        operation=int(input("If you want enter\n 1-Add\n2-Update\n3-Delete\n4-view\n5-Stop"))
#for addin tasks to the task empty list
        if operation==1:
            add=input("Enter the task you want to add:")
            task.append(add)
            print("Task has been successfully added ")
#for updating task by the new one 
        elif operation==2:
            update_val=input("Enter the name you want to update:")
            if update_val in task:
                up=input("Enter the new task:")
                ind=task.index(update_val)
                task[ind]=up
                print(f"{update_val} is Updated as {up}")
#for deleting the task from the task list
        elif operation==3:
            del_val=input("Which task you want to delete:")
            if del_val in task:
                ind=task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted")
#for view all the ask from the task list
        elif operation==4:
            print(f"total task={task}")

# do end the program        
        elif operation==5:
            print("Thank you")
            break
        else:
            print("You enterd invalid input")

task()