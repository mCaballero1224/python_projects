print("Welcome to the Computer Quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

score = 0

questions = ["CPU", "GPU", "RAM", "PSU", "SSD", "HDD"]
answers = ["central processing unit", "graphics processing unit", "random access memory", "power supply unit", "solid state drive", "hard disk drive"]

print("Okay! Let's play:\n")

for i in range(6):
    answer = input("What does " + questions[i] + " stand for?\n")
    if answer.lower() == answers[i]:
        print("Correct")
        score+=1
    else:
        print("Incorrect!")

if score == 6:
    print("Perfect Score! Great job!")
else:
    print("Final Score: " + str(score) + "/6")
