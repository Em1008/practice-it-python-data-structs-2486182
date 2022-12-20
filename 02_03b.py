from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority
    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

task_queue = deque()

def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_tasks():
    for t in task_queue:
        print(t.taskDesc)

# Can't get this to work properly :(
def task_complete(task):
    return task_queue.remove(task)

def main():
    #add code here
    add_task(Task("Make List"))
    add_task(Task("Make breakfast"))
    add_task(Task("Respond to email", True))
    print_tasks()
    print(do_task())
    task_complete(Task("Make breakfast"))

    return

if __name__ == "__main__":
    main()