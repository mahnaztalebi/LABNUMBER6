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
            new_digit = str((int(number) + 3) % 10) # yields remainder
            encoded_pass += new_digit
        return encoded_pass

    def decode(encoded_pass):
        decoded_pass = ""
        for number in encoded_pass:
            if int(number) <= 2:
                new_digit = str(int(number) + 7)
            else:
                new_digit = str(int(number) - 3)
            decoded_pass += new_digit
        print(f"The encoded password is {encoded_pass}, and the decoded password is {decoded_pass}.")

    while True:
        menu()
        option = input("Please enter an option: ")

        if option == "1":
            pass_to_encode = input("Please enter your password to encode: ")
            encoded_pass = encode()
            print("Your password has been encoded and stored!\n")
            continue

        elif option == "2":
            decode(encoded_pass)

        elif option == "3":
            break

if __name__ == "__main__":
    main()
