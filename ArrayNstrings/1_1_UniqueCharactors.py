def isUniqueCharactors(chars):
    ## Assumptions: only ASCII is used
    if(len(chars) >128):
        print("False")
        return False
    array = [False for _ in range(128)]
 
    for char in chars:
        ## Store the values in charactor ASCI value as a key
        if( array[ord(char)] is not False):
            print("False @"+char)
            return False
        else:
            array[ord(char)] = True
            print("True @"+char)


name = "asdfghkjlqwertyi"

print(isUniqueCharactors(name))