# Stage 1: Identifying the sounds and factors

# - The following part of the code demonstrates the factors 3, 5, 7 being assigned sounds:

sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

#  Return the sound effects assigned to factors.

def raindrops(number):
    return [sounds for a, sounds in sound_factors.items() if number % a == 0]

# .items() method returns all dictionary keys with values.

def convert(number):
    return " ".join(raindrops(number)) or str(number)

# " ".join(raindrops(number)) is a form of concatenation with the elements of a iterable.

print(convert(28))