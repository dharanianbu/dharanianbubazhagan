# your code goes here
#Take the input from the user:   
lower = int(input(" "))  
upper = int(input(" "))  
 
for num1 in range(lower ,upper  + 1):  
   if num1 > 1:  
       for i in range(2,num1):  
           if (num1 % i) == 0:  
               break  
       else:  
           print(num1)  
