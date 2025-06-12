# Task Tracker

Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## How to run

Clone the repository and run the following command:

```bash
git clone https://github.com/KeshavMukundan/task-tracker.git
cd backend-projects/task-tracker
```

Run the following command to build and run the project:

```bash

# To add a task
python task-tracker.py add "Buy groceries"

# To update a task
python task-tracker.py update 1 "Buy groceries and cook dinner"

# To delete a task
python task-tracker.py delete 1

# To mark a task as in progress/done/todo
python task-tracker.py mark-in-progress 1
python task-tracker.py mark-done 1
python task-tracker.py mark-todo 1

# To list all tasks
python task-tracker.py list
python task-tracker.py list done
python task-tracker.py list todo
python task-tracker.py list in-progress
```
