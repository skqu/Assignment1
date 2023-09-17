# Trin 3: Fejlhåndtering
# Nu skal vi ind i første fejlhåndtering – dette bliver uden exception dem tager vi bagefter. 
# 1.	Identificere mulige fejl: Noter de fejl som i kan forstille jer en bruger laver, som vil være dumt på en lommeregner Hint: tænk både matematisk f.eks. kvadratroden af -1 men også rent brugen af systemet, gir det mening at subtrahere strenge. 
# Potential error could be the following: 
#   1. Division by zero - 5/0
#   2. Calculate with wrong type - "2" + 2
#   3. Unknown operation - 6%8
#   4. Input format - 5++2
# 2.	Pseudo kode: Vi skal tilpasse vores pseudo kode, så vi ved hvornår vi muligvis fejler. Hint: tænk løsninger på fejlene ind. 
# if input is not numbers then
#   tell user the input is not valid
# else if the operation is unknown then
#   tell user the operation is not valid
# else if wrong input format then
#   Type in valid input formai
# else if division then
#   if second number is 0 then
#       tell user that division with zero is not valid
# perfrom calculation and inform user
# 3.	Tilføj den første fejlhåndtering: Lav nu de nødvendige ændringer i koden. Hint: test den godt igennem, måske virker den ikke som I forventer. 
str_first = input("Type in the first number and hit enter: ")
str_op = input("Type in the operation and hit enter: ")
str_second = input("Type in the second number and hit enter: ")
if __name__ == "__main__":
    list_int = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list_operation = ["+", "/", "-", "*"]
    list_input = [str_first, str_second]
    int_index = 0
    for str_input in list_input:
        for i in str_input:
            if i not in list_int:
                exit("This calculator only takes numeric input")
    if str_op not in list_operation:
        exit("Not valid operation")

    int_first = int(str_first)
    int_second = int(str_second)

    # 4.	Tilføj resten: Når I har styr på den første så tilføj de resterende. Hint: Ligesom med operationer, sikre jer at den første virker før i går videre.  
    if str_op == "+":
        print(int_first + int_second)
    elif str_op == "-":
        print(int_first - int_second)
    elif str_op == "*":
        print(int_first * int_second)
    elif int_second == 0:
        print("Division by zero is not permitted")
    elif str_op == "/":
        print(int_first/int_second)
    else:
        print("Cannot calculate - an unexpected error happen")
