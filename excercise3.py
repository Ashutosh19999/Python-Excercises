#This is a python guess game where a player has to guess the number within a limited no of guesses.The number 'n' which is to be guessed can be set to any number.
n = 78
guesses = 9
guesses1=1
print("Welcome to the number guessing game.")
print("Rules:")
print("1.There is a hidden number which you have to guess")
print("2.You will have total of 9 guesses.")
print("3.If you are able to get the number you win.")
print("4.But, if youn are not able to guess the number and no of guesses are over then, you lose.")
print("The range is between 50-100")
while 1:
    print("No of guesses left:", guesses)
    print("Guess the number:")
    number = int(input())
    if number < n:
        guesses = guesses - 1
        guesses1=guesses1 + 1
        print("Number is lesser than actual number.Please guess the number again.")
        if guesses == 0:
            print("You  used all the  guesses and was not able to guess the number.")
            print("Number of guesses used", guesses1-1)
            print("You lose!!!")
            break
        else:
            continue

    if number > n:
        guesses = guesses - 1
        guesses1=guesses1 + 1
        print("Number is greater than actual number.Please guess the number again.")
        if guesses == 0:
            print("You  used all the  guesses and was not able to guess the number.")
            print("Number of guesses used",guesses1-1)
            print("You lose!!!")
            break
        else:
            continue

    elif number == n:
        print("Number you guessed is correct.")
        print("Number is",n)
        print("Number of guesses you took:",guesses1)
        print("You win!!!")
        break
