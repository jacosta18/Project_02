sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

factors = (3, 5, 7)

def divisible (number, divisor):
    return number % divisor == 0

def raindrops(number):
    return [sound_factors[factors]
            for factors in factors
            if divisible(number, factors)]

def convert(number):
    say = raindrops(number)
    return " ".join(say) if say else str(number)

print(convert(30))

