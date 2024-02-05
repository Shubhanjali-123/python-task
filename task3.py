# 3. *Quiz Application:* Design a quiz that challenges users with multiple-choice 
# questions from various categories. Store questions and answers in lists or dictionaries, 
# track scores, and provide feedback on results.

print("*Quiz Application:*")
score=0
Quiz_1=input("['1. Who developed Python Programming Language?']\n a) Wick van Rossum \n b) Rasmus Lerdorf \n c) Guido van Rossum \n d) Niene Stom \nAnswer:")
if Quiz_1 =="c" or Quiz_1 == "Guido van Rossum":
    score=score+1
    print("{'correct'}")
    print("score",score)
else:
    print("score",score)
    print("{'incorrect'}")

Quiz_2=input("['2. Which type of Programming does Python support?']\n a) object-oriented programming\n b) structured programming\n c) functional programming\n d) all of the mentioned \nAnswer:")
if Quiz_2 =="d" or Quiz_2 == "all of the mentioned":
    score=score+1
    print("{'correct'}")
    print("score",score)
else:
    print("score",score)
    print("{'incorrect'}")

Quiz_3=input("['3. Is Python case sensitive when dealing with identifiers?'] \n a) no \n b) yes \n c) machine dependent \n d) none of the mentioned\n Answer:")
if Quiz_3 =="b" or Quiz_3 == "yes":
    score=score+1
    print("{'correct'}")
    print("score",score)
else:
    print("score",score)
    print("{'incorrect'}")

Quiz_4=input("['4. Which of the following is the correct extension of the Python file?']\n a) .python \n b) .pl \n c) .py \n d) .p \nAnswer:")
if Quiz_4 =="c" or Quiz_4 == ".py":
    score=score+1
    print("{'correct'}")
    print("score",score)
else:
    print("score",score)
    print("{'incorrect'}")

Quiz_5=input("['5. Is Python code compiled or interpreted?']\n a) Python code is both compiled and interpreted\n b) Python code is neither compiled nor interpreted\n c) Python code is only compiled\n d) Python code is only interpreted\nAnswer:")
if Quiz_5 =="a" or Quiz_5 == "Python code is both compiled and interpreted":
    score=score+1
    print("{'correct'}")
    print("score",score)
else:
    print("score",score)
    print("{'incorrect'}")

#Provide feedback on results.
if score<=1:
    print("your total score is:",score,"your score is low!")
elif score==2:
    print("your total score is",score,"your score is good!")
else:
    print("your total score is",score,"your score is verygood")



