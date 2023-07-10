class ToDoList:
    """
    A simple to-do list application.

    Methods:
    - add_task(task): Add a task to the to-do list.
    - remove_task(task): Remove a task from the to-do list.
    - view_tasks(): View all the tasks in the to-do list.
    """

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the to-do list.

        Parameters:
        - task (str): The task description.

        Returns:
        None
        """
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        """
        Remove a task from the to-do list.

        Parameters:
        - task (str): The task description.

        Returns:
        None
        """
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")

    def view_tasks(self):
        """
        View all the tasks in the to-do list.

        Parameters:
        None

        Returns:
        None
        """
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found!")


# Main Program
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n======= To-Do List App =======")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

"""
OUTPUT:
======= To-Do List App =======
1. Add Task
2. Remove Task
3. View Tasks
4. Quit
Enter your choice (1-4): 1
Enter the task: Code review
Task added successfully!

======= To-Do List App =======
1. Add Task
2. Remove Task
3. View Tasks
4. Quit
Enter your choice (1-4): 3
To-Do List:
1. Code review

======= To-Do List App =======
1. Add Task
2. Remove Task
3. View Tasks
4. Quit
Enter your choice (1-4):      

"""