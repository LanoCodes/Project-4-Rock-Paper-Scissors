import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps_choice_string = input('***Welcome to Rock, Paper, Scissors***\nChoose 0 for Rock, 1 for Paper, and 2 for Scissors!!\n')
rps_choice = int(rps_choice_string)
comp_rps_choice = random.randint(0,2)

game_choice = [rock, paper, scissors]

print('You chose:\n')
print(f'{game_choice[rps_choice]}')
print('Computer chose:\n')
print(f'{game_choice[comp_rps_choice]}')


if comp_rps_choice == rps_choice:
  print('It was a draw.')

if rps_choice == 0:
  if comp_rps_choice == 1:
    print('Paper beats rock...\nYou lose.')
  else:
    print('Rock beats scissors!\n\tYou win.')
elif rps_choice == 1:
  if comp_rps_choice == 2:
    print('Scissors beats paper...\nYou lose.')
  else:
    print('Paper beats rock!\n\tYou win.')
elif rps_choice == 2:
  if comp_rps_choice == 0:
    print('Rock beats scissors...\nYou lose.')
  else:
    print('Scissors beats paper!\n\tYou win.')
else:
  print('HEY! That wasn\'t one of the choices...')