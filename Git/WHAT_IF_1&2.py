import numpy as np
import matplotlib.pyplot as plt

def speedPred():
    x = avg

    print("\n\n\n\033[4mReaction Speed Predictor\033[0m\n")
    print("For this, we will use your previous concentration level of ",x,"/10\n")
    print("This code will predict your reaction speed based on your current concentration level.\nLogically, the better your concentration - the more likely you are to perform at your best, and score highly in the game.\nThis code will assume that a mood level of 10 is equal to the average reaction speed of the average human (300ms).")


    y =  float(550 - 25*x)     #formula to determine reaction speed based on mood level

    y = int(y)

    plt.scatter(x, y, label="Calculated Concentration Level")

    plt.xlabel("Concentration level (1-10)")
    plt.ylabel("Reaction speed (ms)")
    plt.title("Predicted reaction speed based on concentration level")

    def graphPlot():
        plt.scatter([], [], color=label_color, label=label_text)
        plt.legend()
        plt.grid(True)

        
        plt.show()


    if x > 3 and x < 8:
        print("\nBased on your concentration level, we predict your average reaction speed to be approximately",y,"ms.")
        print("That is a decent score! You can assume that your concentration level right now is \033[1mgood\033[0m.")
        plt.gca().set_facecolor('lightblue')  
        label_text = f"Good reaction speed ({y} ms reaction time)"  
        label_color = 'lightblue'
        graphPlot()
        
    elif x > 7 and x <= 10:
        print("\nWow! You must feel great! Based on your concentration level, we predict your average reaction speed to be approximately",y,"ms.")
        print("That is a great score! You can assume that your concentration level right now is \033[1mhigh\033[0m.")
        plt.gca().set_facecolor('lightgreen')  
        label_text = f"Great reaction speed ({y} ms reaction time)"  
        label_color = 'lightgreen'
        graphPlot()
    elif x >= 1 and x < 4:
        print("\nOh. You must feel very poor! Based on your concentration level, we predict your average reaction speed to be approximately",y,"ms.")
        print("That is a low score! You can assume that your concentration level right now is \033[1mmediocre\033[0m.")
        plt.gca().set_facecolor('red')  
        label_text = f"Poor reaction speed ({y} ms reaction time)"   
        label_color = 'red'
        graphPlot()
        
    else:
        print("\nInvalid. A concentration level of", x,"is not between 1 and 10.")


print("\033[4m'WHAT IF' QUESTION 1:\033[0m\n")
print("\033[1mDISCLAIMER:\033[0m When you want to move onto question 2, close the graph from question 1.\n")
print("What would your reaction speed be if you based your concentration level on your sleep quantity, mood level and the climate status?\n")
sleep_time = int(input("How many hours did you sleep last night?: "))
mood = int(input("How do you feel right now? (On a scale from 1 to 10): "))
climate = int(input("How good was the climate today? (On a scale from 1 to 10): "))

sleep_quality = 2.5*sleep_time-10

avg = (sleep_time+mood+climate)/3 
avg = round(avg,1)
if avg < 1:
    avg = 1
print("\nCurrent concentration level: ",avg,"/10")

speedPred()

print("\n\n\n\n\n\n\033[4m'WHAT IF' QUESTION 2:\033[0m\n")
print("What would your reaction speed be if you based your concentration level on your age, how physically active you are and how mentally active you are?\n")
age = int(input("What age are you?: "))
p_active = int(input("How physically active are you on a scale from 1 to 10? \n- 1 being you don't do any exercise and 10 being you exercise everyday of the week (physical exercises such as running, gym, sports etc.): "))
m_active = int(input("How mentally active are you on a scale from 1 to 10? \n- 1 being you don't do any mental exercises and 10 being you exercise everyday of the week (mental exercises such as chess, crosswords, maths etc.): "))



if age >= 35:
    y = -(1/5)*(age) +17
elif age < 35:
    y = (1/5)*(age) +3



avg = (y+p_active+m_active)/3 
avg = round(avg,1)
if avg < 1:
    avg = 1
print("\nCurrent concentration level: ",avg,"/10")

speedPred()
