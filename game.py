import random;

def Random_choice():
  return random.choice(['rock','scissor','paper']);

def Convert_input(your_choice):
  if your_choice == 1:
    your_choice = 'rock';
  elif your_choice == 2:
    your_choice = 'scissor';
  elif your_choice == 3:
    your_choice = 'paper';
  else:
    print("Invalid input");

  return your_choice;

def Play(computer_choice, your_choice):
  if computer_choice == your_choice:
    print("TIE");
  elif computer_choice == 'scissor' and your_choice == 'rock':
    print("WIN");
  elif computer_choice == 'rock' and your_choice == 'paper':
    print("WIN");
  elif computer_choice == 'paper' and your_choice == 'scissor':
    print("WIN");
  else:
    print("Computer wins!");

def Main():
  print(" 1 - rock \n 2 - scissor \n 3 - paper \n");
  computer_choice = Random_choice();
  your_choice = Convert_input(int(input("Choose: ")));
  Play(computer_choice, your_choice);
  print("Computer choice:" + computer_choice);
  print("Your choice:" + your_choice);

Main();
