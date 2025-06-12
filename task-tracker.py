from datetime import datetime
import json
import sys
import os


def load_tasks():
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json") as f:
                return json.load(f)
        except Exception as e:
            print(e)
    return []




def save_tasks(tasks):
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(e)
def current_time():
    return datetime.now().strftime("%H:%M:%S")


def load_count():
    if os.path.exists("count.json"):
        with open("count.json") as f:
            count = json.load(f)
            return count
    else:
        return {"count": 1}
    
def save_count(count):
    with open("count.json", "w") as f:
        count_json = {"count": count}
        json.dump(count_json, f)

        
    
def add_task(desc):
    tasks = load_tasks()
    count = load_count()
    task = {"id": count["count"], "description": None, "status": None, "createdAt": None, "updatedAt": None}
    task["description"] = desc
    task["createdAt"] = current_time()
    task["status"] = "todo"
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")
    count["count"] += 1
    save_count(count["count"])
    

def update_task(id, desc):
    task = load_tasks()
    for i in task:
        if i["id"] == int(id):
            i["description"] = desc
            i["updatedAt"] = current_time()
            save_tasks(task) 
            print("Task successfully updated")

def delete_task(id):
    task = load_tasks()
    for i in task:
        if i["id"] == int(id):
            task.remove(i)
            save_tasks(task)
            print("Task successfully removed")

def mark_task_done(id):
    task = load_tasks()
    for i in task:
        if i["id"] == int(id):
            i["status"] = "Done"
            print("Task marked as 'Done' successfully")
            save_tasks(task)
            break
    else:
        print(f"{id} not in tasks")
            

def mark_task_prog(id):
    task = load_tasks()
    for i in task:
        if i["id"] == int(id):
            i["status"] = "in-progress"
            print("Task marked as 'in-progress' successfully")
            save_tasks(task)

            break
    else:
        print(f"{id} not in tasks")

def display_all_tasks():
    task = load_tasks()
    if len(task) == 0:
        print("No tasks")
    for i in task:
        print(f"ID: {i['id']}")
        print(f"Description: {i['description']}")
        print(f"Status: {i['status']}")
        print(f"Created At: {i['createdAt']}")
        print(f"Updated At: {i['updatedAt']}")
        print("---------------------------------")



def display_task_byStatus(status):
    flag = False
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == status:
            print_tasks(task)      
            flag = True      
    if not flag:
        match(status):
            case "todo":
                print("You have completed all the tasks")
            case "in-progress":
                print("You don't have any tasks in progress")
            case "Done":
                print("You have not completed any tasks")
                    
def print_tasks(task):
    
    print(f"ID: {task['id']}")
    print(f"Description: {task['description']}")
    print(f"Status: {task['status']}")
    print(f"Created At: {task['createdAt']}")
    print(f"Updated At: {task['updatedAt']}")
    print("---------------------------------")
            
def main():
    args = sys.argv

    match(args[1]):
        case "add":
            desc = args[2]
            add_task(desc)
        case "update":
            id = args[2]
            desc = args[3]
            update_task(id, desc)
        case "list":
            if len(args) == 2:
                display_all_tasks()
            elif args[2] == "todo":
                display_task_byStatus("todo")   
            elif args[2] == "in-progress":
                display_task_byStatus("in-progress")
            elif args[2] == "done":
                display_task_byStatus("Done")
           
        case "delete":
            id = args[2]
            delete_task(id)
        case "mark-in-progress":
            id = args[2]
            mark_task_prog(id)
        case "mark-done":
            id = args[2]
            mark_task_done(id)
       

        



if __name__ == "__main__":
    main()