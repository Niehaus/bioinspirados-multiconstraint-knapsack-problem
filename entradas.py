# -*- coding: utf-8 -*-
# Python3 code to demonstrate  
# to compute all possible permutations 
# using list comprehension  

#create file
file_obj  = open("arguments.txt", "w+")
  
# initiaizing lists 
ants = [10, 25, 50, 75, 100] 
iterations = [50, 75, 85, 95, 100] 
alpha = [1, 0.5, 1, 1, 1.25]
beta = [51, 1,0.5, 1.25, 1.0]

# printing lists  
print ("A lista de parametros são: " + str(ants) +
                               " " + str(iterations) + 
                               " " + str(alpha) +
                               " " + str(beta)) 
  
# using list comprehension  
# to compute all possible permutations 
res = [[i, j, k, l] for i in ants  
                 for j in iterations 
                 for k in alpha
                 for l in beta] 

  
# printing result 
#print ("All possible permutations are : " +  str(res)) 
string_form = ""
for combination in res:
    for argument in combination:
        string_form += " " + str(argument)
    string_form += "\n"

print("Todas as combinações foram escritas com sucesso!")
file_obj.write(string_form)
