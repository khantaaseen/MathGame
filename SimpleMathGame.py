#taaseen khan
#project 1


from sys import exit
import random




def difficulty(user_difficulty):
    
    if user_difficulty == 1:
        numbers = (random.randint(0,9), random.randint(0,9))
    elif user_difficulty == 2:
        numbers = (random.randint(10,99), random.randint(10,99))
    elif user_difficulty == 3:
        numbers = (random.randint(100,999), random.randint(100,999))
    return numbers



def operations(user_operation):
    
    sign = ["+","-","*","/"]
    
    if user_operation == 1:
        sign = "+"
    elif user_operation == 2:
        sign = "-"
    elif user_operation ==3:
        sign = "*"
    elif user_operation == 4:
        sign = "/"
    elif user_operation == 5:
        sign = random.choice(sign)
    return sign


def swap(numbers, operation):
    
    numbers_t = numbers
    if operation == "-":
        if numbers_t[0] < numbers_t[1]:
            numbers_t = (numbers_t[1], numbers_t[0])
    elif operation == "/":
        if numbers_t[1] == 0:
            numbers_t = (numbers_t [0],1)
    return numbers_t


def evaluate(numbers, operation):
    
    answer = eval(str(numbers[0]) + operation + str(numbers[1]))
    return answer


def fatigue(correct):
    
    phrase = random.randint(1,4)
    if correct == True:
        if (phrase == 1):
            return "\nVery good!"
        elif (phrase == 2):
            return "\nExcellent!"
        elif (phrase == 3):
            return "\nNice work!"
        else:
            return "\nKeep up the good work!"
    else:
        if (phrase == 1):
            return "\nNo, please try again."
        elif (phrase == 2):
            return "\nWrong, try once more."
        elif (phrase == 3):        
            return "\nDon't give up!"
        else:
            return "\nNo, keep trying."


def main():
    print()
    print("Difficulties:")
    print("---------------")
    print("1: single digit integers\n2: double digit integers\n3: triple digit integers")
    user_difficulty = int(input("Enter difficulty: "))
    correct = 0
    wrong = 0

    while True:
        print("\n1 = addition")
        print("2 = subtraction")
        print("3 = multiplication")
        print("4 = division")
        print("5 = random operation\n")
        user_operation = int(input("Enter desired operation 1-5, or -1 to exit: "))
        print()
        
        if user_operation == -1:
                print("Correct:\n", correct)
                print("Wrong:\n", wrong)
                print("Thanks for playing")
                exit()
        
        numbers = difficulty(user_difficulty)
        sign = operations(user_operation)
        numbers = swap(numbers, sign)
        
        print("What is", str(numbers[0]), "", sign, "", str(numbers[1]) + "?")
        
        answer = round(evaluate(numbers, sign))

        while True:
            user_answer = int(input("Enter an answer or -1 to exit: "))
            if user_answer == -1:
                print("Correct:\n", correct)
                print("Wrong:\n", wrong)
                print("Thanks for playing")
                exit()
                
            if answer == user_answer:
                print(fatigue(True))
                correct += 1
                break
            else:
                print(fatigue(False))
                wrong += 1
                continue
            
main()
            
