
import random

print("WELCOME TO ROCK-PAPER-SCISSORS GAME ")
R='rock'
P="paper"
S="scissors"
varieties=['R','P','S']

while True:
   userChoice=input('Enter a leter from  R,S,P: ')
   if userChoice not in varieties:
      print("error,try again ")
      continue
   else:
      break
cpuChoice=random.choice(varieties)  
print('Cpu turn: '+cpuChoice)
if userChoice== "R" and cpuChoice=='R':
   print("draw")
elif userChoice=="P" and cpuChoice=="P":
   print("draw")
elif userChoice=="S" and cpuChoice=="S":
   print('draw')
elif userChoice=="R" and cpuChoice=="S":
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



