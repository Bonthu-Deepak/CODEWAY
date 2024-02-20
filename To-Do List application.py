tasks=[]

def add_task():
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task Added Successfully")
def view_tasks():
    if len(tasks)==0:
        print("No Tasks...")
    else:
        print("List of Tasks:")
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')

def delete_task():
    if len(tasks)==0:
        print("No Tasks to delete.")
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i + 1}.{task}')
        choice = int(input("Enter the task number to delete:"))
        if 0<choice<=len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully...")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\n*** TO-D0-LIST APPLICATION***")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Quit")

        choice=int(input("Enter your Choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("Thanks for using our to-do list application...")
            break
        else:
            print("Invalid Choice. Please try again")


if __name__=="__main__":
    main()
