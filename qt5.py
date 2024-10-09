def main():
    user_input = input("Enter a string to compress: ")
    print(compress(user_input))


def compress(s):
    frequencies = []
    counter = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            frequencies.append(f"{s[i - 1]}{counter}")
            counter = 1

    frequencies.append(f"{s[-1]}{counter}")
    return ''.join(frequencies)


main()
