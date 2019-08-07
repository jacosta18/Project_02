import formal_code

# To run the App, run 'app.py' (ctrl shift f10) and follow the steps in the output section.

sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

while True:

    def raindrops(number):
        return [sounds for a, sounds in sound_factors.items() if number % a == 0]

    def convert(number):
        return " ".join(raindrops(number)) or str(number)

    num = int(input("Enter number here: "))

    print(convert(num))

    word = input("Would you like to continue? y/n: ")

    if word.lower() == 'n':         # -----------------> If input is 'n' or 'N', the app ends.

        print("We look forward to your return!")

        break

    else:
        print("Okay! Let's go!")

