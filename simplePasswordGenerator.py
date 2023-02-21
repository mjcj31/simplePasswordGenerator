import string
import random


def generate_password() -> str:
    while True:
        # Ask for input size from user
        print("Enter a size for your password (Can only be between 8 and 25 characters)")
        N = input("Size: ")
        # res = ''.join(random.choices(string.ascii_letters + string.punctuation, k=N)) # Only available for python 3.6 or later. Currently using 3.5
        res = ''.join(random.sample(
            string.ascii_letters + string.punctuation, k=int(N)))

        if int(N) < 8 or int(N) > 25:
            print("invalid input, try again")
            continue
        else:
            # print("Generated password : " + str(res))
            # flag = False
            break
    return str(res + '\n')


def save_file():
    # password = generate_password()
    # print(password)
    with open('passwords_generated.txt', 'a') as output:
        output.write(generate_password())


if __name__ == "__main__":
    save_file()


# Extra line

# Extra Line
# Extra Line
