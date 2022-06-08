
import random
print("WELCOME TO ROCK-PAPER-SCISSORS GAME")
print ("R stands for Rock, P stands for Paper, S stands for Scissors")
print("Let\'s begin")
varieties=['R','P','S']
while True:
 while True:
   userChoice=input('Enter a leter from  R,S,P: ')
   if userChoice not in varieties:
      print("error,try again ")
      continue
   else:
      break
 cpuChoice=random.choice(varieties)  
 print('Cpu turn: '+cpuChoice)
 if cpuChoice==userChoice:
   print ('draw')
   continue
 else:
    break
if userChoice=="R" and cpuChoice=="S":
   print("YOU WIN")
elif userChoice=="S" and cpuChoice=="P":
   print("YOU WIN")
elif userChoice=="P" and cpuChoice=="R":
   print("YOU WIN")
elif userChoice=="S" and cpuChoice=="R":
   print("YOU LOSE")
elif userChoice=="P" and cpuChoice=="S":
   print("YOU LOSE")
else:
   print("YOU LOSE")
