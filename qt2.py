def most_frequent_char(input_string):
    frequency = {}
    # Count the frequency of each character in the string
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the character with the highest frequency
    max_count = 0
    most_frequent = None
    for char in input_string:
        if frequency[char] > max_count:
            max_count = frequency[char]
            most_frequent = char
            
    return most_frequent


input_string = "abracadabra"
output_char = most_frequent_char(input_string)
print(output_char)
