def validateStackSequence(pushed, popped):
    
    j = 0
 
   
    stack = []
 
    for x in pushed:
        stack.append(x)
 
        
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j = j + 1
 
    return j == len(popped)
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequence(pushed, popped))
