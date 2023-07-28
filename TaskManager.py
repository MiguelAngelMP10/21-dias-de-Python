class TaskManager:

    def __init__(self):
        self._task_manager = {}

    def addTask(self, task, tags):
        key = task.lower()
        set_tags = set(tags)
        if key in self._task_manager:
            self._task_manager[key] = self._task_manager[key].union(set_tags)
        else:
            self._task_manager[key] = set_tags

    def printTasks(self):
        return self._task_manager
