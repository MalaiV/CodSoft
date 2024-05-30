# (link unavailable)

# Initialize an empty list to store tasks
tasks = []

def show_menu():
	print("1. Show all tasks")
	print("2. Add a task")
	print("3. Update a task")
	print("4. Delete a task")
	print("5. Quit")

def show_tasks():
	for i, task in enumerate(tasks, start=1):
		print(f"{i}. {task}")

def add_task():
	task = input("Enter a task: ")
	tasks.append(task)

def update_task():
	show_tasks()
	task_number = int(input("Enter the task number to update: "))
	new_task = input("Enter the new task: ")
	tasks[task_number - 1] = new_task

def delete_task():
	show_tasks()
	task_number = int(input("Enter the task number to delete: "))
	del tasks[task_number - 1]

while True:
	show_menu()
	choice = input("Choose an option: ")
	if choice == "1":
		show_tasks()
	elif choice == "2":
		add_task()
	elif choice == "3":
		update_task()
	elif choice == "4":
		delete_task()
	elif choice == "5":
		break
	else:
		print("Invalid choice. Please choose a valid option.")

