import json
import os
import random

def task_tracker():
    task_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Tasks")
    if not os.path.exists(task_dir):
        os.makedirs(task_dir)

    while True:

        print("««« Task Tracker V1 »»»")
        print("1. Open.")
        print("2. Close.")

        task1 = input("Select option (1 or 2): ")
        
        if task1 == "1":
            print("««« Main Menu »»»")
            print("1. Task Manager.")
            print("2. Create Tasks.")

            #creats a task

            task1 = input("Select option (1 or 2): ")
            if task1 == "2":
                task_create = input("Type desired task name: ")

                task_status = ("done", "todo", "in-progress") # tuple for status

                task_id = {
                    task_create : random.randrange(1, 100) #Creats unique id
                }

                task_data = {
                    "task_name": task_create,
                    "task_status": task_status[1],
                    "task_id": task_id
                }

                try:
                    task_path = os.path.join(task_dir, f"{task_create}.json")
                    with open(task_path, "x") as f:
                        json.dump(task_data, f, indent=4)
                        print(f"Task added successfully! {task_id[task_create]}") 
                except FileExistsError:
                    print("Task already exists.")

            else:
                print("««« Task Manager »»»")
                print("1. Task list.")
                print("2. Delete Task.")
                print("3. Update Task.")

                task2 = input("Select option (1 to 3): ")

                #lists all created tasks

                if task2 == "1":
                    task_path = os.path.join(task_dir)
                    task_files = [f for f in os.listdir(task_path) if f.endswith('.json')]
                    if not task_files:
                        print("No tasks found.")
                    else:
                        print(task_files)

                #deletes desired tasks

                elif task2 == "2":
                    task_del = input("What task should i delete?")
                    file_path = os.path.join(task_dir, f"{task_del}.json")

                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"{file_path} was sucessfully deleted!")
                    else:
                        print("File does not exist.")

                #changes file status from in-progress to done 

                else:
                    task_updt = input("What task do you want to update? ")
                    file_path = os.path.join(task_dir, f"{task_updt}.json")

                #done change

                    if os.path.exists(file_path):
                        task_updt2 = input("Change status (done, todo or in-progress): ")
                        if task_updt2 == "done":
                            with open(file_path, "r") as f:
                                data = json.load(f)
                                if data["task_status"] == "done":
                                    print("Task status is already \"done\" ")
                                else:
                                    data["task_status"] = "done"
                                    with open (file_path, "w") as f:
                                        json.dump(data, f, indent=4)

                #in progress change

                        elif task_updt2 == "in-progress":
                            with open(file_path, "r") as f:
                                data = json.load(f)
                                if data["task_status"] == "in-progress":
                                    print("Task status is already \"in-progress\" ")
                                else:
                                    data["task_status"] = "in-progress"
                                    with open(file_path, "w") as f:
                                        json.dump(data, f, indent=4)

                #todo change

                        else:
                            with open(file_path, "r") as f:
                                data = json.load(f)
                                if data["task_status"] == "todo":
                                    print("Task status is already \"todo\" ")
                                else:
                                    data["task_status"] = "todo"
                                    with open(file_path, "w") as f:
                                        json.dump(data, f, indent=4)

        else:
            print("Closing Task Tracker V1 ")
            break

if __name__ == "__main__":
    task_tracker()