
name = input('Player Name: ')

print('Welcome ' + name + ' to the a and b game :)')

choice = input ( name + ' are you ready to choose between a and b (yes/no) ' )
score = 0
total_n = 5
print('*************************************************************')
if choice.lower() == 'yes':
    print('1. What Programming Languange is this game using? ')
    print('a. Python')
    print('b. java')
    choice = input ('choice: ')
    if choice.lower() == 'a':
        score += 1
        print (' Good Job ' + name + ' you got the correct answer. ')
    else:
        print(' Nice try ' + name + ' wrong answer')
            
    
    print('*************************************************************')
    print('2. What year python was created? ')
    print('a. 1995')
    print('b. 1991')
    choice = input ('choice: ')
    if choice.lower() == 'b':
        score += 1
        print (' Good Job ' + name + ' you got the correct answer. ')
    else:
        print(' Nice try ' + name + ' wrong answer')

    print('*************************************************************')
    print('3. Who created Python? ')
    print('a. Lebron James')
    print('b. Guido Van Rossum')
    choice = input ('choice: ')
    if choice.lower() == 'b':
        score += 1
        print (' Good Job ' + name + ' you got the correct answer. ')
    else:
        print(' Nice try ' + name + ' wrong answer')

    print('*************************************************************')
    print('4. What is 4*10? ')
    print('a. 40')
    print('b. 39')
    choice = input ('choice: ')
    if choice.lower() == 'a':
        score += 1
        print (' Good Job ' + name + ' you got the correct answer. ')
    else:
        print(' Nice try ' + name + ' wrong answer')


    print('*************************************************************')
    print('5. What is 2+1? ')
    print('a. 3')
    print('b. 4')
    choice = input ('choice: ')
    if choice.lower() == 'a':
        score += 1
        print (' Good Job ' + name + ' you got the correct answer. ')
    else:
        print(' Nice try ' + name + ' wrong answer')
    print('*************************************************************')


else:
    print (' Thankyou ' + name )

    print('*************************************************************')
print("Thank you for playing you got", score ," questions correct.")
total = (score/total_n) * 100

print(name , total)
print('Goodgame '+ name)






