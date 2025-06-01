task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match priority:
    case "high":
        if time_bound == "yes":
              print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound =="no":
            print(f"Reminder: {task} is a medium priority task that is flexible.")
    case "low":
        print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")

    

