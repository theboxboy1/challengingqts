
def main():

    str = input()
    
    print(balanced(str))


def balanced(str):
    l_counter = 0
    r_counter = 0
    for i in str:
        if i == "(":
            l_counter += 1
        elif i == ")":
            r_counter += 1

    return l_counter == r_counter
            


   

main()
