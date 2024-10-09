
def main():

    str = input().lower()
    
    print(palindrome(str))


def palindrome(str):

    if str == str[::-1]:
        return True
    
    return False

main()
