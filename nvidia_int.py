hello!

Return the first unique character in a string, or None if not found. Ex: 'racecarb'

def nonrepeat(x):
    list = {}
    for element in x:
        if element not in list:
            list[element] = 1
        elseif element in list:
            list[element] = list[element] + 1
    
list { r: 2, a: 2, c: 2, e: 1, r: 2, b: 1}

   for element in x:
       if list[element] == 1:
           return element
           
  O(n)
  O(nlog(n))          
  O(n^2)
    
  for element in x:
  
      for element in x:       
           
           
           
 
          
          
 Implement a stack with O(1) push, pop, and min

 Class MinMaxstack:
    stack = []
    min = []
    max = []
    
    # x is an integer
    def Push(x):
        stack.append(x)
        if len(stack) == 0:
            current_min = x
            current_max = x
            min.append(current_min)
            max.append(current_max)
            return
        if max[-1] > x:
            current_max = max[-1]
        else:
            current_max = x
            
        if min[-1] < x:
            current_min = min[-1]
        else:
            current_min = x
        
        max.append(current_max)
        min.append(current_min)    
           
    Pop():
        return stack.pop(), min.pop(), max.pop()
        
    Min():
        return min[-1]
        
    Max():
    ''' returns the max of the stack''' 
        return max[-1]
        
push(1)
push(6)
push(3)
push(2)
push(1)

stack [1,6,3,2,1]
min=  [1,1,1,1,1]

pop() -> 1

pop()
pop()
pop()


 push(3)
   stack = [3]
   min = []
 push(1)
   stack = [3,1]
   min = [] 
 push(5)
   stack = [3,1,5]
   min = []


Node:
    value
    minimum
    next




a{stack(3), minimum(3), b}   b{2, 2, c}  c{5, 2, None}

   
 push(3)
 push(2)
 push(5)
 
 min() --> 2
 pop() --> 5
 pop() --> 2
 min() --> 3 

 
 
 
 