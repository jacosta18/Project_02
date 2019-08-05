
class Raindrops():

    # Class object attribute:

    sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
    }

    factors = (3, 5, 7)

    def __init__(self, number=0, factor=0):

        self.number = number
        self.factor = factor

    # Operations/Acstions ----> Methods

    def divisible(self):
        return self.number

    def raindrops(number):
        return [sound_factors[factors]
            for factors in factors
            if divisible(number, factors)]

    def convert(number):
        say = raindrops(number)
        return " ".join(say) if say else str(number)



