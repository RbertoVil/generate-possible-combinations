import random


def numberSentences():
    #This function ask to the user the number of sentences to use

    while True:
        try:
            numberSent = int(input('Pls enter the number of sentences that you\'ll working on: '))
            break

        except ValueError:
            print("pls enter a integer")

    return(numberSent)
    

def combinations(number):
    #this function defines the number of posible combinations
    posibleComb = 2**number
    return(posibleComb)


def generate(number):
    #This function will generate a string

    string = []

    for i in range(number):
        #decide between 'v' or 'f' to add to the string

        number = random.randint(0,1)
        if number == 1:
            letter = 'v'
        else:
            letter = 'f'
        
        string.append(" " + letter + " ")

    #verify if the string is in the list.

    verify = list.count(string)

    if verify == 0:
        return(string)
    else:
        return(False)


def begin(numberSentence):
    #begin to generate the list

    count = 0
    posibleComb = combinations(numberSentence)

    while True:
        begin = generate(numberSentence)

        if count == posibleComb:
            break

        elif begin == False:
            pass

        else:
            count += 1   
            list.append(begin)


list = []


def main():
    
    print("Hi, this program has the objetive of find the number of possible combinations of sentences in a truth table")
    print("This could be very helpfull at propositional logic")

    numberSentence = numberSentences()
    
    begin(numberSentence)

    list.sort(reverse=True)

    print("")

    for i in list:
        print(i)

    print("\nTotal of possible combinations: " + str(len(list)))

if __name__ == '__main__':
    main()

