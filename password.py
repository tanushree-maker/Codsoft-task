import random
import string

def generate_password(length):
    """generate a random password of the given length."""
    if length < 1:
        return "Password length must be at least 1."
    
    #define the character sets 
    letters = string.ascii_letters
    digits =string.digits
    special_characters = string.punctuation

    #Combine all the character sets
    all_characters = letters + digits + special_characters

    #Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("welcome to the password generator !")


    try:
        length = int(input("Enter the desired length of the password :"))
    except ValueError:
        print("Invalid input.Please enter a valid integer.") 
        return
    #generate and display the password
    password = generate_password(length)
    print(f"Generated password :{password}")  
    #Run the main function 
if __name__ == "__main__":
    main()
