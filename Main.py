# Numerology calculation for a given name

# Mapping of letters to numerology numbers
numerology_map = {
    1: "AJS",
    2: "BKT",
    3: "CLU",
    4: "DMV",
    5: "ENW",
    6: "FOX",
    7: "GPY",
    8: "HQZ",
    9: "IR"
}

# Mapping of numbers to planets
planet_map = {
    1: "Sun",
    2: "Moon",
    3: "Jupiter",
    4: "Rahu",
    5: "Mercury",
    6: "Venus",
    7: "Ketu",
    8: "Saturn",
    9: "Mars"
}

# Create a letter to number lookup
letter_to_number = {}
for number, letters in numerology_map.items():
    for letter in letters:
        letter_to_number[letter] = number

def numerology_number(name):
    total = 0
    for char in name.upper():
        if char in letter_to_number:
            total += letter_to_number[char]
    return total

def reduce_to_single_digit(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def get_planet(number):
    return planet_map.get(number, "Unknown")

if __name__ == "__main__":
    name = input("Enter a name: ")
    total = numerology_number(name)
    single_digit = reduce_to_single_digit(total)
    planet = get_planet(single_digit)
    print(f"{single_digit}={planet}")