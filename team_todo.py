print("Team to-do list")
def show_menu():
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark done")
    print("4.Quit")
def add_task(tasks):
    name=input("Task name?")
    if user not in tasks:
        tasks[user]={}
    tasks[user][name]="pending"
    save_tasks(tasks)
    print(tasks[user])
def view_tasks(tasks):
    if user not in tasks:
        print("No tasks yet")
    else:
        for name in tasks[user]:
            print(name,"-",tasks[user][name])
def mark_done(tasks):
    name=input("Which task is done?")
    if user in tasks and name in tasks[user]:
        tasks[user][name]="done"
        save_tasks(tasks)
        print("Task marked done")
    else:
        print("Task not found")
def load_tasks():
    tasks = {}
    try:
        file = open("C:/Users/svams/python-practice/team_tasks.txt", "r")
        for line in file:
            owner, name, status = line.strip().split(",")
            if owner not in tasks:
                tasks[owner] = {}
            tasks[owner][name] = status
        file.close()
    except FileNotFoundError:
        pass
    return tasks
def save_tasks(tasks):
    file = open("C:/Users/svams/python-practice/team_tasks.txt","w")
    for owner in tasks:
        for name in tasks[owner]:
            file.write(owner + "," + name + "," + tasks[owner][name] + "\n")
    file.close()
tasks = load_tasks()
user = input("Your name?")
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
