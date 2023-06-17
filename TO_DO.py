import os,time

todo = []

def view_all():
  print("☑️  To-Do List")
  print()
  for row in todo:
    for i in row:
      print(i)
    
def view_priority(): 
  typePriority = input("Search for high, medium, or low priority. > ")
  print(f"☑️  To-Do List - Priority: {typePriority}")

  if typePriority == 'high':
    for row in todo:
      for i in row:
        if 'high' in i:
          for item in row:
            print(item)


  elif typePriority == 'medium':
    for row in todo:
      for i in row:
        if 'medium' in i:
          for item in row:
            print(item)

  elif typePriority == 'low':
    for row in todo:
      for i in row:
        if 'low' in i:
          for item in row:
            print(item)

def changeToDo():
    change = input("Which to-do item would you like to edit? ")
    print()
    for sublist in todo:
        for i, item in enumerate(sublist):
            if change in item:
                specificChange = input("What would you like to change about it? (priority or due date) > ")
                if specificChange == "due date":
                    newDueDate = input("Enter the new due date: ")
                    sublist[i] = sublist[i].replace("due date:", "due date: " + newDueDate)
                elif specificChange == "priority":
                    newPriority = input("Enter the new priority: ")
                    sublist[i] = sublist[i].replace("priority:", "priority: " + newPriority)
          
          
          
        
        
        
          
          
          
          

def menu():
  global todo
  while True:
    choice = input("""⭐️Life Organizer⭐️
  
Welcome to life organizer.
Would you like to add, view, or edit a 'to do' ? """)
    if choice.strip().lower() == 'add':
      subList = []
      todo.append(subList)
      next_q = input("What would you like to add? > ")
      subList.append(next_q.capitalize())
      subList.append('_____')
      due_date = input("When is it due? > ")
      subList.append('due date: '+ due_date)
      priority = input("What's the priority(high, medium, or low)? > ")
      subList.append('priority: ' + priority + '\n')
      print()
      print("Thanks, this task has been added.")
      print()
    if choice.strip().lower() == 'view':
      view_choice = input('Sure do you want to view by priority or view all ? (priority , all) > ')
      if view_choice.strip() == 'all':
        view_all()
        time.sleep(10)
        os.system('clear')
      elif view_choice.strip() ==  'priority':
        view_priority()
        time.sleep(10)
        os.system('clear')
    if choice.strip().lower() == 'edit':
      print()
      view_all()
      print()
      changeToDo()
      view_all()
      time.sleep(10)
      os.system('clear')
        
        

menu()

    