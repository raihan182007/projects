print("=== To do list ===")
print("__________________")

tasks = []
def add_tasks():
    n = input("How many task you want to add? ")
    if n.isdigit():
        n = int(n)
        for _ in range(n):
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.✅")
    else:
        print("❌ Invalid input.❌")

def show_tasks():
    if not tasks:
        print("\n❌ No task found!❌")
    else:
        print("\n⬇️  Tasks:⬇️")
        for i in range(len(tasks)):
            print(f"{i + 1}-{tasks[i]}")


def delete():
    del_task = input("Enter the task you want to delete: ")
    if del_task in tasks:
        tasks.remove(del_task)
        print("Task has been deleted.✅")
    else:
        print("❌ No such task found!❌")

    
def main():
    while True:
        print("\n1.Add tasks")
        print("2.Show tasks")
        print("3.delete tasks")
        print("4.exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_tasks()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("Goodbye!👋👋")
            quit()
        else:
            print("\n❌ Invalid input.Try again.❌")
            continue
main()



