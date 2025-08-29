import json
import os

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
            print("1. View Tasks.")
            print("2. Create Tasks.")

            task1 = input("Select option (1 or 2): ")
            if task1 == "2":
                task_create = input("Type desired task name: ")
                try:
                    task_path = os.path.join(task_dir, f"{task_create}.json")
                    with open(task_path, "x") as f:
                        json.dump({"task_name": task_create}, f)
                except FileExistsError:
                    print("Task already exists.")


            
           
        else:
            print("Closing Task Tracker V1 ")
            break

if __name__ == "__main__":
    task_tracker()