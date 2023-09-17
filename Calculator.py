#Du skal oprette en simpel lommeregner i Python, i første skridt skal den kun tage imod input og addere dem.
# 1.	Pseudo kode: Første skridt er at overveje hvordan koden skal se ud, til dette bruger vi pseudo kode. Her skriver man koden, som hvis man vil forklare den. 
# If user input then
#   add it to new user input
# output the result from the two numbers
# 2.	Tag imod input: Næste skridt er at tage imod input fra brugeren. Til dette bruges funktionen input(). Hint: print dit input så du kan se om det virker 
int_first = int(input("Type in the first number to be added: "))
# 3.	Tag imod tal: Tredje skridt er at tage imod to tal fra brugeren. Disse skal bruges til vores addition. Hint: Begge tal skal bruges senere, så vi skal gemme dem i koden.
int_second = int(input("Type in the second number to be added: "))  
# 4.	Print Resultat: Læg nu de to tal sammen, og udskriv resultatet til brugeren. Hint: string + string eller integer + integer
if __name__ == "__main__":
    str_result = str(int_first + int_second)
    print(str_result)