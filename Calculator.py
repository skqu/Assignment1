#Trin 2: Tilføj de andre operationer
#Nu skal vi udvide vores lommeregner, således den kan bruge alle vores operationer. 
#1.	Pseudo kode: Vi skal tilpasse vores pseudo kode, således vi har styr på alle vores operationer. Hint: vær opmærksom på hvordan man ser forskel fra de fire operationer.
# take equation as input
# if addition add number
# else if subtraktion subtract numbers
# else if multiplication then multiply numbers
# else divide number 
#2.	Tilføj de fire operationer: Lav nu de nødvendige ændringer i koden. Hint: tilføj en operation ad gangen, det er lettere at fejlsøge på to operationer i stedet for fire.
int_first = int(input("Type in the first number and hit enter: "))
str_op = input("Type in the operation and hit enter: ")
int_second = int(input("Type in the second number and hit enter: ")) 
#3.	Tilføj de fire operationer: Lav nu de nødvendige ændringer i koden. Hint: tilføj en operation ad gangen, det er lettere at fejlsøge på to operationer i stedet for fire. 
if __name__ == "__main__":
    if str_op == "+":
        print(int_first + int_second)
    elif str_op == "-":
        print(int_first - int_second)
    elif str_op == "*":
        print(int_first * int_second)
    else:
        print(int_first/int_second)
