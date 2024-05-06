import re

# Given a string of text, return a vector of the first two numbers in it
def extract_numbers(s):
    # This pattern matches numbers that are not immediately preceded by a dot.
    # It ignores numbers that are part of a decimal value.
    pattern = r'(?<!\.)\b\d[\d,]*(?:\w)?\b'

    # Find all matching numbers
    matches = re.findall(pattern, s)

    # Remove any non-digit trailing characters, commas, and convert to integers
    numbers = [int(re.sub(r'[^\d]', '', match)) for match in matches]

    return numbers[:2]

"""
# Example string
input_string = "$565.0 #$40,000 65 $%$7,000 +7.56 $2"
print(extract_numbers(input_string))


# Test cases
test1 = "$55,000.00/yr - $67,000.00/yr"
test2 = "$30,000"
test3 = "$543 65 &56"
test4 = "$54000.00 erf 65,000.01"
test5 = "$70m in funding from"
test6 = "$80,000-$95,000, with"

print(extract_numbers(test1))  # Output: [55000, 67000]
print(extract_numbers(test2))  # Output: [30000]
print(extract_numbers(test3))  # Output: [543, 65]
print(extract_numbers(test4))  # Output: [54000, 65000]
print(extract_numbers(test5))
print(extract_numbers(test6))
"""