
def IsAnagram(s:str, t:str)->bool:
    #First 3 if statements handle errors and edge cases
    #The else statement converts the inputs to ascii, sorts, and gives the results of entry-by-entry comparison
    if(len(s)!=len(t)): 
        return False
    if (s=="" or t==""):
       print("Error: One or both entries were blank")
       return False
    if(s.isspace() or t.isspace()):
        print("Error: IsAnagram cannot parse strings with spaces")
        return False
    else:
        s_ascii=[]
        t_ascii=[]
        for character in s:
            s_ascii.append(ord(character))
        for character in t:
            t_ascii.append(ord(character))
        s_ascii_sorted=sorted(s_ascii)
        t_ascii_sorted=sorted(t_ascii)
        for i in range(0, len(s_ascii_sorted)):
            if(s_ascii_sorted[i]!=t_ascii_sorted[i]):
                return False
            if(i==(len(s_ascii_sorted)-1)):
                return True

print(IsAnagram("coast","coas"))