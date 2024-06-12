def user_input():
    print('Hello input an integer below and the program will test if it is odd or even')
    test_value = input("Enter your integer:")
    print('Thank you, running program...\n')
    return test_value

def test(test):
    try: 
        type(test) == int
        if int(test) % 2 == 0:
            print(f'{test} is even.\n')
            test_again()
        else:
            print(f'{test} is odd.\n')
            test_again()
    except:
        print('You have not entered an integer. Please Enter a whole number with no dot and no letters\n \n')
        print("..........................................")
        main()

def test_again():
    print('Would you like to test another number? y/n')
    again = input()
    if again == 'y':
        main()
    elif again == 'n':
        print('Thanks')
        exit()
    else:
        print("Seems like you haven't entered y or n.")
        print('Exiting program...')
        exit()
    


def main():
    test_value = user_input()
    result = test(test_value)

main()