sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

def raindrops(number):
    return [sounds for a, sounds in sound_factors.items() if number % a == 0]

def convert(number):
    return " ".join(raindrops(number)) or str(number)

print(convert(30))