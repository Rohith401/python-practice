print("My to-do list")
def show_menu():
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark done")
    print("4.Quit")
def add_task(tasks):
    name=input("Task name?")
    tasks[name]="pending"
    save_tasks(tasks)
    print(tasks)
def view_tasks(tasks):
    for name in tasks:
        print(name,"-",tasks[name])
def mark_done(tasks):
    name=input("Which task is done?")
    if name in tasks:
        tasks[name]="done"
        save_tasks(tasks) 
        print("Task marked done")
    else:
         print("Task  not found")
def load_tasks():
    tasks = {}
    try:
        file = open("C:/Users/svams/python-practice/tasks.txt", "r")
        for line in file:
            name, status = line.strip().split(",")
            tasks[name] = status
        file.close()
    except FileNotFoundError:
        pass
    return tasks    
def save_tasks(tasks):
    file = open("C:/Users/svams/python-practice/tasks.txt","w")
    for name in tasks:
        file.write(name + "," + tasks[name] + "\n")
    file.close()
tasks = load_tasks()
while True:
    show_menu()
    choice=input("Choose 1-4:")
    if choice=="1":
        add_task(tasks)   
    elif choice=="2":
        view_tasks(tasks)    
    elif choice=="3":
        mark_done(tasks)  
    elif choice=="4":
        break
    

