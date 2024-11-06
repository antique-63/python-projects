# To-Do List App using Python

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
    
    def add_task(self):
        task = input("\nEnter the task you want to add: ")
        self.tasks.append(task)
        print(f"Task '{task}' has been added.")

    def remove_task(self):
        try:
            self.show_tasks()
            task_num = int(input("\nEnter the number of the task you want to remove: "))
            if task_num < 1 or task_num > len(self.tasks):
                print("Invalid task number.")
            else:
                removed_task = self.tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' has been removed.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n--- To-Do List App ---")
            print("1. Show tasks")
            print("2. Add task")
            print("3. Remove task")
            print("4. Exit")
            
            choice = input("Choose an option: ")

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Initialize and run the To-Do App
if __name__ == "__main__":
    app = ToDoApp()
    app.run()
