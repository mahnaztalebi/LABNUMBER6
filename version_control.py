# Maryam Talebi
def main():
    def menu():
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

    def encode():
        encoded_pass = ''
        for number in pass_to_encode:
            new_digit = str(int(number) + 3)
            encoded_pass += new_digit
        return encoded_pass

    while True:
        menu()
        option = input("Please enter an option: ")

        if option == "1":
            pass_to_encode = input("Please enter your password to encode: ")
            encode()
            print("Your password has been encoded and stored!\n")
            continue

        elif option == "2":
            pass

        elif option == "3":
            break

if __name__ == "__main__":
    main()





'''def main():
        while True:
            menu()
            option = input("Please enter an option: ")

            if option == "1":
                global pass_to_encode
                pass_to_encode = input("Please enter your password to encode: ")
                global encoded_pass
                encoded_pass = ''
                for number in pass_to_encode:
                    new_digit = str(int(number) + 3)
                    encoded_pass += new_digit
                print("Your password has been encoded and stored!\n")
                continue

            elif option == "2":
                print(f"The encoded password is {encoded_pass}, and the original password is {pass_to_encode}.\n")
                continue

            elif option == "3":
                break'''