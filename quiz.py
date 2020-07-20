import random
#Implement a "master loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
# Create a class, then create at least one object of that class and populate it with data  
def get_tof_questions():

    questions = []
    questions.append(["Darth Vader said, Luke, I am your father", "F"])
    questions.append(["Tiger King Documentary is only on Hulu", "F"])
    questions.append(["Krystal is a Kardashian sister", "F"])
    questions.append(["Snow White was the first Disney Princess", "F"])
    questions.append(["Harry Potter was a Horcrux", "T"])
    questions.append(["Dolly Parton is Miley Cyrus godmother", "T"])
    questions.append(["Abraham Lincoln was born in Kentucky", "T"])
    questions.append(["Did Michael Crichton write Jurassic Park", "T"])
    questions.append(["There are fourteen Real Housewives shows", "T"])
    questions.append(["Yearly Americans eat 3 billion pizzas", "T"])
    
    return questions

def play_tof_quiz():

        tof_questions = get_tof_questions()

        random.shuffle(tof_questions)

#player score 
        score = 0

#create a for loop
        for q in tof_questions:

            print("True or false: " + q[0])
            guess = raw_input("Enter T or F: ")
     
            if guess.lower() == q[1].lower():
                print("Correct")

            elif guess.lower() != q[1].lower():
                print("Incorrect")

 
         
        else:
            print("Incorrect :This is not acceptable!")

#print final score
        print("Your Citizenship Quiz Score is: " + str(score))
        
play_tof_quiz()