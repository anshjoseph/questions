def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0   
    i = 0    
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1
 
    return j == m
virus_cop = input()
number_of_people = int(input())
data = list()
for _ in range(number_of_people):
   temp = input()
   if len(temp) == len(set(temp).intersection(set(virus_cop))):
      
        if isSubSequence(temp, virus_cop):
            data.append('POSITIVE')
        else:
            data.append('NEGATIVE')
   else:
       data.append('NEGATIVE')
del(temp)
print(end="\n",*data)
    
    
