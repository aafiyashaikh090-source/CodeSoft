import random
import string

def generate_password(length,use_uppercase=True, use_digits=True, use_special=True):

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_lowercase
        #now generating the pswd
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("pswd generator")

    while True:
        try:
            length = int(input("enter the length of pswd(minimum 1)-"))
            if length < 1:
                print("length must be at least 1,try again please")
                continue
            break
        except ValueError:
            print("invalid input,please enter positive integer")

            #for complex pswd we are using the options
    use_uppercase = input("include uppercase letters?(yes/no,default y):").lower().strip() != 'no'
    use_digits = input("include the digits?(yes/no,default y):").lower().strip() != 'no'
    use_special = input("include special characters?(yes/no,default y):").lower().strip() != 'no'

            #now generate & display the pswd 
    password = generate_password(length, use_uppercase,use_digits,use_special)
    print(f"generated password: {password}")

if __name__ == "__main__":
    main()
