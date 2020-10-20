print("Title of program: Response Bot!")
print()
while True:
  description = input("Hello! I am your personal Response Bot! How are you feeling today?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
 <<<<<<< patch-2
      encouragement_list.append("interesting")
        
    =======
      encouragement_list.append("I hope the day treats you better! There's always something called tomorrow. :3")
 >>>>>>> main
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you should stay positive, stay strong!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you could take a break or nap, you deserve it after all you've done!")
      counter += 1

  if counter == 0:
    
      output = "Sorry, I do not understand. Try reiterating what you have said in simpler terms!"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
