


def main():

    

    str = input()
    
    print(longest(str))
    
    


def longest(str):

    words = str.split()

    sorted_list = sorted(words, key = len, reverse = True)

    if len(sorted_list[0]) == len(sorted_list[1]):
        if words.index(sorted_list[0]) < words.index(sorted_list[1]):
            return sorted_list[0]
        
        else:
            return sorted_list[1]


    return words


            
  

main()
