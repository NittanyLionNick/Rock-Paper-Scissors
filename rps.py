p1 = input("PLAYER 1: Enter (R)ock, (P)aper, or (S)cissors: ")
p2 = input("PLAYER 2: Enter (R)ock, (P)aper, or (S)cissors: ")
print("Player 1 chooses", p1, "and player 2 chooses", p2)
if ((p1 == "P") and (p2 == "R")):
   print("Paper covers rock")
   print("Player 1 wins!")
elif ((p2 == "P") and (p1 == "R")):
   print("Paper covers rock")
   print("Player 2 wins!")
elif ((p1 == "R") and (p2 == "S")):
   print("Rock breaks scissors")
   print("Player 1 wins!")
elif ((p2 == "R") and (p1 == "S")):
   print("Rock breaks scissors")
   print("Player 2 wins!")
elif ((p1 == "S") and (p2 == "P")):
   print("Scissors cut paper")
   print("Player 1 wins!")
elif ((p2 == "S") and (p1 == "P")):
   print("Scissors cut paper")
   print("Player 2 wins!")
elif (p1 == p2):
   print("Tie!")
else:
   print("INVALID INPUT!")
