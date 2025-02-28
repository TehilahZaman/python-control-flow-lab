# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input('Enter a letter ').lower()

    if len(letter) > 1 or not letter.isalpha():
        print("Invalid: input is not a letter")
        return 

    vowels = ["a", "e", "i", "o", "u"]

    if letter in vowels: 
        print(f"The Letter {letter} is a vowel")
    elif letter not in vowels:
        print(f"Letter {letter} is not a vowel")  
   

check_letter()

# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    age = int(input('Enter youre age '))

    minimum_age = 18; 

    if age >= minimum_age: 
        print("You can vote")
    elif age < 0:
        print("Not a valid age")
    else: 
        print("You're too young to vote")    

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    dog_age = int(input("Enter your dog's age "))

    if dog_age == 1:
        dog_years = 10
    elif dog_age == 2:
        dog_years = 20
    elif dog_age > 2: 
        dog_years = 20 + (dog_age - 2) * 7
    else:
        print("Not valid")
        return     
    
    print(f"Your god is {dog_years} years old in human years")

calculate_dog_years()

# Exercise 4: Weather Advice

def weather_advice():
    yes = True
    no = False 
    
    q1 = input("Is the weather cold? ").lower() == "yes"
    q2 = input("Is it raining? ").lower() == "yes"

    if q1 and q2:
        print("Wear a waterproof coat.")
    elif q1 and not q2:
        print("Wear a warm coat.")
    elif not q1 and q2:
        print("Carry an umbrella.")
    else: 
        print("Wear light clothing.")

weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    season = None
    winter = ["dec", "jan", "feb", "mar"]
    spring = ["mar", "apr", "may", "jun"]
    summer = ["jun", "jul", "aug", "sep"]
    fall = ["sep", "oct", "nov", "dec"]

    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = int(input("Enter the day of the month: "))

    
    if ((month == "jan" or month == "feb") or ((month == "dec" and day >= 21) or (month == "mar" and day <= 19))): 
       season = "Winter"
    elif (month == "jan" or month == "feb") or ((month == "mar" and day >= 20) or (month == "jun" and day <= 21)): 
       season ="Spring"
    elif (month == "jun" and day >= 21) or (month == "jul" or month == "aug") or (month == "sep" and day <= 21):
        season = "Summer"   
    elif (month == "sep" and day >= 22) or (month == "oct" or month == "nov") or (month == "dec" and day <= 20):
        season = "Fall"
    else: 
       ("Invalid please try again")
       
    print(f"{month} {day} is in {season}")

determine_season()


# Exercise 6: Number Guessing Game

def guess_number():
   turn = 0 
   number = 20
   while turn <= 5: 
        if turn == 5:
            print("Sorry, you failed to guess the number in five attempts.")
            break 

        guess = int(input("Guess a number 1- 100 "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        elif guess == number:
            print("Congratulations, you guessed correctly!" )
            break

        turn += 1
                      
    
guess_number()