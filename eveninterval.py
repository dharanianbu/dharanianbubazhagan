# your code goes here
# Python program to print Even Numbers in given range 
  
start = int(input(" ")) 
end = int(input(" ")) 
  
# iterating each number in list 
for num in range(start+1, end + 1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ") 
