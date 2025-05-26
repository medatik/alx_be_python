task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
tb = input("Is it time-bound? (yes/no)")

match priority :
    case "high" :
        if tb == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else :
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if tb == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else :
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if tb == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else :
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
