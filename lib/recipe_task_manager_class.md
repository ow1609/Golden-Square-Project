Task Manager Class Design Recipe

1. Describe the Problem

Put or write the user story here. Add any clarifying notes you might have.

<!-- As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list. -->

# Clarifying notes:

make a list of tasks, mark task as complete 

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class TaskManager():
    # User-facing properties:
    #   task: string 
    #   self.task_list = []

    def __init__(self):
        # Parameters:
        #   none
        # Side-effects
        #   none
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   add task to self.task_list
        pass # No code here yet

    def remove_completed_task(self, task):
        # Returns:
        #   nothing
        # Side-effects:
        #   remove task from self.task_list
        pass # No code here yet

    def show_task_list(self):
        # returns formated string f'Task list: {self.task_list}'
        

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# given no task

task = TaskManager()
task.show_task_list() => No tasks to complete

# given a single task
task = TaskManager()
task.add_task("walk the dawg") 
task.show_task_list() => Task list: walk the dawg

# given 2 tasks
task = TaskManager()
task.add_task("walk the dog")
task.add_task("water the plants")
task.show_task_list() => Task list : walk the dog and water the plants

# given more than 2 tasks
task = TaskManager()
task.add_task("walk the dog")
task.add_task("water the plants")
task.add_task("wash the dishes")
task.show_task_list() => Task list : walk the dog, water the plants and wash the dishes

# remove a completed task with only 2 tasks to begin with
task = TaskManager()
task.add_task("walk the dog")
task.add_task("water the plants")
task.remove_completed_task("walk the dog")
task.show_task_list() => Task list: water the plants

# remove a completed task with more than 2 tasks to begin with
task = TaskManager()
task.add_task("walk the dog")
task.add_task("water the plants")
task.add_task("wash the dishes")
task.remove_completed_task("water the plants")
task.show_task_list() => Task list : walk the dog and wash the dishes

# remove all tasks as completed
task = TaskManager()
task.add_task("walk the dog")
task.add_task("water the plants")
task.remove_completed_task("water the plant")
task.remove_completed_task("walk the dog")
task.show_task_list() => No tasks to complete

# if a non string is passed in
task = TaskManager()
task.add_task(34628)
raise exception with error message =>'Invalid input, please enter text'

# attempt to remove a task that is not on the list 
task = TaskManager()
task.add_task("water the plants")
task.remove_task("Walk the dog")
raise exception with error message 'Error: this task does not exist'


Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.


