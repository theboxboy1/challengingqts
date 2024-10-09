


def main():

    

    str1 = input().lower()
    str2 = input().lower()

    
    print(anagram(str1,str2))
    
    


def anagram(str1, str2):

    return sorted(str1) == sorted(str2)
    

            
  

main()
