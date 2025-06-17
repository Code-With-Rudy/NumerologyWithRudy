# Mapping based on the image
numerology_chart = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

vowels = {'A', 'E', 'I', 'O', 'U'}

def reduce_to_single_digit_or_master(num):
    if num in {11, 22, 33}:
        return num
    while num > 9:
        num = sum(int(d) for d in str(num))
    return num

def calculate_numerology(name):
    name = name.upper().replace(" ", "")
    
    all_letters_sum = 0
    vowels_sum = 0
    consonants_sum = 0

    for ch in name:
        if ch in numerology_chart:
            val = numerology_chart[ch]
            all_letters_sum += val
            if ch in vowels:
                vowels_sum += val
            else:
                consonants_sum += val

    destiny_number = reduce_to_single_digit_or_master(all_letters_sum)
    soul_urge_number = reduce_to_single_digit_or_master(vowels_sum)
    personality_number = reduce_to_single_digit_or_master(consonants_sum)

    return {
        "Destiny Number": destiny_number,
        "Soul Urge Number": soul_urge_number,
        "Personality Number": personality_number
    }

# Main
full_name = input("Enter your full name: ")
result = calculate_numerology(full_name)

print("\nNumerology for:", full_name)
for key, value in result.items():
    print(f"{key}: {value}")
