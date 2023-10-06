class TaskManager():

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if type(task) is not str:
            raise Exception('Invalid input, please enter text')
        else:
            self.task_list.append(task)
        return self.task_list

    def remove_completed_task(self, task):
        if task not in self.task_list:
            raise Exception('Error: this task is not on your task list')
        return self.task_list.remove(task)


    def show_task_list(self):
        self.formatted_task_list = 'Task list:'
        if len(self.task_list) == 0:
            self.formatted_task_list = 'No tasks to complete'
        if len(self.task_list) == 1:
            self.formatted_task_list += f' {self.task_list[0]}'
        elif len(self.task_list) == 2:
            self.formatted_task_list += f' {self.task_list[0]} and {self.task_list[1]}'
        else:
            for i in self.task_list[:-2]:
                self.formatted_task_list += f' {i},'
                self.formatted_task_list += f' {self.task_list[-2]} and {self.task_list[-1]}'
        return self.formatted_task_list
        
        