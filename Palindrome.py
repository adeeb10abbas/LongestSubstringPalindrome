
def longest_palindrome(string):
    try:
        copy = string.split(" ")
        string = string.lower()
        s = string.split(" ")
        counter = 0
        diction = {}
        list = []
        list2 = []
        for i in s:
            if i == i[::-1]:
                diction[i] = copy[counter]
                list.append(i)
            
           
            counter += 1
        for k in list:
            list2.append(len(k))
            
        tk = list2.index(max(list2))
        coming = list[tk]
        return diction[coming]
    except:
        return "There are no palindromic terms in this one"
        
        
        

    
print(longest_palindrome("anarchy"))
