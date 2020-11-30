tasks = {'task0': 'Introductory card', 'task1': 'Mindmap Game', 'task2': '?', 'task3': 'Profit!'}

while True:
   print('Enter a name: (blank to quit)')
   self = input()
   day = "task" + str(self)
   print (day)
   if self == '':
      break

   if day in tasks:
      print(tasks[day] )
   else:
      print('No information for task' + day)
      
   """  bday = input()
   birthdays[name] = bday
   print('Birthday database updated.') """