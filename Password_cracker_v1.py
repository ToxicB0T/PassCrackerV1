import pyfiglet
import hashlib
import string
import itertools
import time

# Formatting The Project Name
print(pyfiglet.figlet_format("PassCrackerV1", font="slant"))

# Main Function
def main():
    while True:
        print("\n\tWelcome to PassCracker")
        print("\nChoose an option:\n")
        print("1. Brute Force")
        print("2. Hash Cracking")
        print("3. Exit")
        x= int(input("\n"))
        if x == 1:
            brute_force()
        elif x == 2:
            hash_cracking()
        elif x == 3:
            print("Exiting the program...")
            break
        else:
            print("Enter a valid option")

# Brute Force Function
def brute_force():
    hashed_pass = input("Enter the Hashed Password: ")
    chars = string.ascii_letters + string.digits + string.punctuation
    start = time.time()
    for pass_length in range(1, 5):
        for x in itertools.product(chars, repeat=pass_length):
            guessed_pass = ''.join(x)
            hashed_guessed_pass = hashlib.md5(guessed_pass.encode()).hexdigest()
            if hashed_guessed_pass == hashed_pass:
                end = time.time()
                total_time = end - start
                print("\nPassword successfully cracked. The password is: {}".format(guessed_pass))
                print("Time taken: {:.2f} seconds".format(total_time))
                return
    print("\nFailed to crack the password with brute force.")
    print("The password length is higher than 4")

# Hash Cracking Function
def hash_cracking():
    hashed_pass = input("Enter the Hashed Password: ")
    file_path = input("Enter the full path of the file: ")
    start = time.time()
    try:
        with open(file_path.strip(), 'r', encoding='ISO-8859-1') as f: # encoding='ISO-8859-1' => Prevent UnicodeDecodeError
            for passwd in f:
                hashed_guess = hashlib.md5(passwd.strip().encode()).hexdigest()
                if hashed_pass == hashed_guess:
                    end = time.time()
                    total_time =  end - start
                    print("\nPassword successfully cracked. The password is: {}".format(passwd.strip()))
                    print("Time taken: {:.2f} seconds".format(total_time))
                    return
    except FileNotFoundError:
        print("\nError: The file was not found. Please check the path and try again.")
        return
    except Exception as e:
        print("\nAn error occurred: {e}".format(e))
        return
    end = time.time()
    total_time = end - start
    print("\nFailed to crack the password. Try another file...")  
    print("Time taken: {:.2f} seconds".format(total_time))


if __name__ == "__main__":
    main()