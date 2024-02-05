#1. *Text-Based Adventure Game:* Create an interactive story where the player makes 
# choices that shape the narrative. Use variables, conditional statements, and loops to 
# construct the branching paths and outcomes.

print("*Text-Based Adventure Game:*")
answer_yes=['yes','y','Yes','Y','YES']
answer_no=['no','NO','N','n','not','Not','NOT']
print("""welcome!*Text-Based Adventure Game:*
     you are going to office in your car when you see a woman in dirty clothes running towords you and asking for a ride office.
      will you give her a ride office,(yes/no)
       """)
a=input('enter yes or no:')
if a in answer_yes:
    print('after 5 min i will stopped at checkpoint so police ask you if you seen a suspicous woman.will you say(yes/no)\n')
    b=input('enter yes or no:')
    if b in answer_yes:
        print('you are honest person.she was a murderer & you won the game\n')
    elif b in answer_no:
        print('you helped a murderer. now go to jail.Game over\n')
    else:
        print('you have typed wrong input.Goodbye/n:')

elif a in answer_no:
    print('now she is trying to kill you.will you knock her down?(yes/no)\n')
    c=input('enter yes or no:')
    if c in answer_yes:
        print('Congrats she is murderer and you helped the police.\n:')
    elif c in answer_no:
        print('you have dead beacuase she is murderer.game over\n')
    else:
        print('you have wrong typed.Good bye\n')
else:
    print('you typed wrong input .Good bye\n')