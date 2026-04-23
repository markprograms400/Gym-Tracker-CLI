import os 
import json

def load_data():
  if os.path.isfile("data.json"):
    with open("data.json", "r") as file:
      data = json.load(file)
  else: 
    data = {}
  return data 

def save_data(data):
  with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

def menu(data):
    print("""MENU:
1. Add workout 
2. View workout
3. Exit 
""")
    while True:
      user_choice = input("What would you like to do?: ")
      if user_choice == "1": 
        add_workout(data)
      elif user_choice == "2":
        view_workout(data)
      elif user_choice == "3":
        break
      else: 
        print("Error: Wrong choice ")

def add_workout(data):
  while True: 
    exercise = input("Exercise: ")
    weight = input("Weight: ")
    sets = input("Sets: ")
    reps = input("Reps: ")
    date = input("Date: ")
    entry = {
      "Weight": weight,
      "Sets": sets,
      "Reps": reps,
      "Date": date
    }

    if exercise not in data:
      data[exercise] = []
    data[exercise].append(entry)
    save_data(data)
    print("Saved data to data.json!")

    resume = input("Continue? (y/n): ").lower()
    if resume == "y":
      continue
    if resume == "n":
      break
    else: 
      print(resume)


def view_workout(data):
  if not data: 
    print("No workouts") 
    return
  for exercise in data:
    workout = data[exercise]
    latest = exercise, workout[-1]
    print(latest)

data = load_data()
menu(data)

