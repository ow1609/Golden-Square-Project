from lib.task_manager_class import *
import pytest

# given no task
def test_given_no_task():
    task = TaskManager()
    result = task.show_task_list()
    assert result == 'No tasks to complete'

# given a single task
def test_given_single_task():
    task = TaskManager()
    task.add_task("walk the dawg") 
    result = task.show_task_list()
    assert result == 'Task list: walk the dawg'

# given two tasks
def test_given_two_tasks():
    task = TaskManager()
    task.add_task("walk the dawg")
    task.add_task("water the plants")
    result = task.show_task_list()
    assert result == 'Task list: walk the dawg and water the plants'

# given more than two tasks
def test_given_more_than_two_tasks():
    task = TaskManager()
    task.add_task("walk the dog")
    task.add_task("water the plants")
    task.add_task("wash the dishes")
    result = task.show_task_list()
    assert result == 'Task list: walk the dog, water the plants and wash the dishes'


# remove a completed task with only 2 tasks to begin with
def test_remove_a_completed_task_with_only_two_tasks_to_begin_with():
    task = TaskManager()
    task.add_task('walk the dog')
    task.add_task('water the plants')
    task.remove_completed_task('walk the dog')
    result = task.show_task_list() 
    assert result == 'Task list: water the plants'

# remove a completed task with more than 2 tasks to begin with
def test_remove_a_completed_task_with_more_than_two_tasks_to_begin_with():
    task = TaskManager()
    task.add_task("walk the dog")
    task.add_task("water the plants")
    task.add_task("wash the dishes")
    task.remove_completed_task("water the plants")
    result = task.show_task_list()
    assert result == 'Task list: walk the dog and wash the dishes'

# remove all tasks as completed
def remove_all_tasks_as_complete():
    task = TaskManager()
    task.add_task("walk the dog")
    task.add_task("water the plants")
    task.remove_completed_task("water the plant")
    task.remove_completed_task("walk the dog")
    result = task.show_task_list()
    assert result == 'No tasks to complete'

# if a non string is passed in
def test_given_non_string():
    with pytest.raises(Exception) as e:
        task = TaskManager()
        task.add_task(34628)
    error_message = str(e.value)
    assert error_message == 'Invalid input, please enter text'


# attempt to remove a task that is not on the list 
def test_attempt_to_remove_a_task_that_is_not_on_the_list():
    with pytest.raises(Exception) as e:
        task = TaskManager()
        task.add_task("water the plants")
        task.remove_completed_task("Walk the dog")
    error_message = str(e.value)
    assert error_message == 'Error: this task is not on your task list'