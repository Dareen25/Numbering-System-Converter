#Dareen Elsayed Ragab        20231052
#Malak Hussein Mohammed      20230415
#Mirna Mahmoud El-Hefny Ali  20231185

# convert_from_decimal_to_binary
def convert_from_decimal_to_binary(num):

    binary = ""
    while num != 0:
        binary = str(num % 2)+ binary
        num //= 2
    return binary
#to convert from octal to binary
def convert_from_octal_to_binary(num):
    binary = " "  # to store the binary numbers
    for digit in num: #for every digit in the number
        binary_digit = " " #to represent every number in 3 digits
        digit = int(digit)

        for i in range(3):
            binary_digit = str(digit % 2) + binary_digit
            digit = digit // 2

        binary += binary_digit

#removing what leads to zeros by finding the first '1'
        first_one_index = binary.find('1')
        if first_one_index != -1:
            binary = binary[first_one_index:] #to remove zeroes until it find '1'
    return binary
#to convert from hexadecimal to binary
def convert_from_hexadecimal_to_binary(num):
    binary = " "  # to store the binary numbers


    for digit in num:  # for every digit in the number
# to convert the hexadecimal number into decimal number
        if "0" <= digit <= "9":
            digit = int(digit)
        else:
            digit = ord(digit.upper()) - ord("A") + 10  # it converts the alphabet to capital, then convert it into its number using ASCI

        binary_digit = " "  # to represent every number in 4 digits


# to convert from hexadecimal to binary
        for i in range(4):
            binary_digit = str(digit % 2) + binary_digit
            digit = digit // 2

        binary += binary_digit
    return binary
# convert_from_decimal_to_octal
def convert_from_decimal_to_octal(num):
    octal = ""
    while num != 0:
        remainder = num % 8
        octal = str(remainder)+ octal
        num //= 8
    return octal
# convert from octal to decimal
def convert_from_octal_to_decimal(num):
    dec, power = 0, 0
    while num != 0:
        remainder = num % 10
        dec = dec + (remainder * (8 ** power))
        num = num // 10
        power += 1
    return dec

# convert from decimal to hexadecimal
def convert_from_decimal_to_hexadecimal(num):
    converting_dict = {
         0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
         6: "6", 7: "7", 8: "8", 9: "9", 10: "A",
         11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
        }
    hexa = ""
    while num != 0:
        remainder = num % 16
        hexa += converting_dict[remainder]
        num //= 16
    return hexa[::-1]
# convert_hexadecimal_to_decimal
def convert_hexadecimal_to_decimal(num):
    num = num.upper()
    hex_char = "0123456789ABCDEF"
    dec = 0
    for digit in num:
        dec = dec * 16 + hex_char.index(digit)
    return dec



# convert from hexadecimal to octal
def convert_from_hexadecimal_to_octal(num):

# convert from hexadecimal to decimal
        hex_char = "0123456789ABCDEF"
        decimal_version = 0
        for digit in num:
            decimal_version = decimal_version * 16 + hex_char.index(digit)

# convert from decimal to binary
        s = ""  # to store the binary numbers
        while decimal_version != 0:
            r = decimal_version % 2  # remainder
            s = str(r) + s
            decimal_version = decimal_version // 2


# to add 0 if the lenght less than 3 digits
        s = '0' * (3 - len(s) % 3) + s

# convert from binary to octal
        oc = " "  # to store the octal numbers
        i = 0
        while i < len(s):
            octal_digit = s[i:i+3][::-1]  # to make a group of 3 digits from right to left

            decimal_value = 0
            for power, digit in enumerate(octal_digit):  # to calculate each digit in the group
                decimal_value += int(digit) * (2**power)

            oc += str(decimal_value)
            i = i+3
        return oc

# convert from octal to hexadecimal
def convert_from_octal_to_hexadecimal(num):
    binary = ''  # to store the binary numbers

# convert from octal to binary
    for digit in num:  # for every digit in the number
        binary_digit = ''  # to represent every number in 3 digits
        digit = int(digit)

        for i in range(3):
            binary_digit = str(digit % 2) + binary_digit
            digit = digit // 2

        binary += binary_digit

# removing what leads to zeros by finding the first '1'
        first_one_index = binary.find('1')
        if first_one_index != -1:
            binary = binary[first_one_index:]  # to remove zeroes until it find '1'

# to convert from binary to hexadecimal
    # to add zero if number's lenght is less than 4
    while len(binary) % 4 != 0:
        binary = "0" + binary

    hexa = ""  # to store the hexadecimal numbers
    i = 0

    while i < len(binary):
        hexa_digit = binary[i:i+4][::-1]  # to take every 4 digits from right to left
        decimal_value = 0

        for power, digit in enumerate(hexa_digit):  # for every digit in the group
            decimal_value += int(digit) * (2**power)

# to convert decimal number to hexadecimal
        if decimal_value < 10:
            hexa += str(decimal_value)
        else:
            hexa += chr(ord("A") + decimal_value - 10)

        i = i + 4
    return hexa





# convert from binary to decimal
def convert_from_binary_to_decimal(num):
    dec, power = 0, 0
    while num != 0:
        remainder = num % 10
        dec = dec + remainder * 2 ** power
        power += 1
    return dec

# to convert from hexadecimal to binary
def convert_from_binary_to_octal(num):

# to add 0 if the number lenght is less than 3
    while len(num) % 3 != 0:
        num = "0" + num

    oc = ""  # to store the octal numbers
    i = 0
    while i < len(num):
        octal_digit = num[i:i+3][::-1]  # to get a group of 3 digits from right to left
        decimal_value = 0

        for power, digit in enumerate(octal_digit):  # for every digit in the group
                decimal_value += int(digit) * (2**power)

        oc += str(decimal_value)
        i = i + 3
    return oc
# convert_from_binary_to_hexadecimal
def convert_from_binary_to_hexadecimal(num):
    # to add zero if number's lenght is less than 4
    while len(num) % 4 != 0:
        num = "0" + num

    hexa = ""  # to store the hexadecimal numbers
    i = 0
    while i < len(num):
        hexa_digit = num[i:i + 4]
        decimal_value = 0

        for power, digit in enumerate(hexa_digit[::-1]):  # for every digit in the group
            decimal_value += int(digit) * (2 ** power)

        # to convert decimal number to hexadecimal
        if decimal_value < 10:
            hexa = str(decimal_value) + hexa
        else:
            hexa = chr(ord("A") + decimal_value - 10) + hexa

        i = i + 4

    return hexa[::-1]

# check the decimal number is valid or not
def check_dec(num):
    valid_set = "0123456789"
    while not all(bit in valid_set for bit in num):
        num = input("Enter a valid octal number please ")
    return num




# check the binary number is valid or not
def check_bin(num):
    valid_set = "01"
    while not all(bit in valid_set for bit in num):
        num = input("Enter a valid binary number please ")
    return num


# check the octal number is valid or not
def check_octal(num):
    valid_set = "01234567"
    while not all(bit in valid_set for bit in num):
        num = input("Enter a valid octal number please ")
    return num


# check the hexadecimal number is valid or not
def check_hexa(num):
    valid_set = "0123456789ABCDEFabcdef"
    while not all(bit in valid_set for bit in num):
        num = input("Enter a valid hexadecimal number please ").upper()
    return num


# menu 1
def show_menu_1():
    print("** numbering system converter **")
    print("A) Insert a new number")
    print("B) Exit program")

# menu 2
def show_menu_2():
    print("** Please select the base you want to convert a number from **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")

# menu 3
def show_menu_3():
    print("** Please select the base you want to convert a number to **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")


while True:
    print()
    show_menu_1()
    choice = input("Please enter your choice (A or B):").upper()

    if choice == "A":
        number = input("Please insert a number:").upper()
        while True:
            print()
            show_menu_2()
            choice_menu2 = input("Please enter your choice(A,B,C,D):").upper()
            if choice_menu2 in ["A", "B", "C", "D"]:
                break
            else:
                print("Please select a valid choice")


        if choice_menu2 == "A":
            number = check_dec(number)
        elif choice_menu2 == "B":
            number = check_bin(number)
        elif choice_menu2 == "C":
            number = check_octal(number)
        elif choice_menu2 == "D":
            number = check_hexa(number)


        while True:
            print()
            show_menu_3()
            choice_menu3 = input("Please enter your choice(A,B,C,D):").upper()
            if choice_menu3 in ["A", "B", "C", "D"]:
                break
            else:
                print("Please select a valid choice")


        if choice_menu2 == "A" and choice_menu3 == "B":
            res = convert_from_decimal_to_binary(int(number))
            print("The binary value:", res)
        elif choice_menu2 == "C" and choice_menu3 == "B":
            res = convert_from_octal_to_binary(number)
            print("The binary value:", res)
        elif choice_menu2 == "D" and choice_menu3 == "B":
            res = convert_from_hexadecimal_to_binary(number)
            print("The binary value:", res)

        elif choice_menu2 == "A" and choice_menu3 == "D":
            res = convert_from_decimal_to_hexadecimal(int(number))
            print("The hexadecimal value:", res)
        elif choice_menu2 == "B" and choice_menu3 == "D":
            res = convert_from_binary_to_hexadecimal(number)
            print("The hexadecimal value:", res)
        elif choice_menu2 == "C" and choice_menu3 == "D":
            res = convert_from_octal_to_hexadecimal(number)
            print("The hexadecimal value:", res)


        elif choice_menu2 == "A" and choice_menu3 == "C":
            res = convert_from_decimal_to_octal(int(number))
            print("The octal value:", res)
        elif choice_menu2 == "B" and choice_menu3 == "C":
            res = convert_from_binary_to_octal(number)
            print("The octal value:", res)
        elif choice_menu2 == "D" and choice_menu3 == "C":
            res = convert_from_hexadecimal_to_octal(number)
            print("The octal value:", res)

        elif choice_menu2 == "B" and choice_menu3 == "A":
            res = convert_from_binary_to_decimal(int(number))
            print("The decimal value:", res)
        elif choice_menu2 == "C" and choice_menu3 == "A":
            res = convert_from_octal_to_decimal(int(number))
            print("The decimal value:", res)
        elif choice_menu2 == "D" and choice_menu3 == "A":
            res = convert_hexadecimal_to_decimal(number)
            print("The decimal value:", res)



    elif choice == "B":
        print("Exiting the program")
        break
    else:
        print("Please select a valid choice")
        continue










