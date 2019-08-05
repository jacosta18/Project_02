# Stage 1: Identifying the sounds and factors

# - The following part of the code demonstrates the factors 3, 5, 7 being assigned sounds:

sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

factors = (3, 5, 7)

while True:


    num = int(input("Enter a number here: "))

    # Stage 2: Returning True if the divisor is a factor of the number

    def divisible (number, divisior):
        return number % divisior == 0

    #print(divisible(35,5))

    # Running the above print statement, Python would return 'True' as 5 is a factor of 35.

    # Stage 3: Return the sound effects assinged to factors.

    def raindrops(number):
        return [sound_factors[factors]
                for factors in factors
                if divisible(number, factors)]

    #print(raindrops(30))

    # The print statement about would return ['Pling', 'Plang] because factors 3 and 5 are factors of 30.
    # The ouput is also a string.

    # Stage 4: Return a string by using " ".join().

    def convert(number):
        say = raindrops(number)
        return " ".join(say) if say else str(number)

    print(convert(num))

    word = input("Would you like to continue (yes/no)?")

    if word == 'no':

        print("Thank you, Goodbye!")
        break

    else:
        print("Welcome back!")


