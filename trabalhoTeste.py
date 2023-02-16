#Author - Iftekhar Ahmed Arnab
#North East University Bangladesh, CSE

def print_in_format(matrix):
    for i in range(9):
        if i%3==0 and i>0:
            print("")
        print(str(matrix[i])+" ", end = "")

def count(s):
    c = 0
    ideal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]
    
    for i in range(9):
        if s[i]!=0 and s[i]!=ideal[i]:
            c+=1
    return c


def move(ar, p, st):
    rh = 9999
    store_st = st.copy()
    
    for i in range(len(ar)):
        
        dupl_st = st.copy()
        
        tmp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = tmp
        
        trh = count(dupl_st)
        
        if trh<rh:
            rh = trh
            store_st = dupl_st.copy()
    
    #print(rh, store_st)
    
    return store_st, rh
    
    
state = [1, 2, 3,
         0, 5, 6,
         4, 7, 8]

h = count(state)
Level = 1

print("\n------ Level "+str(Level)+" ------")
print_in_format(state)
print("\nHeuristic Value(Misplaced) : "+str(h))


while h>0:
    pos = int(state.index(0))
    
    Level += 1
    
    if pos==0:
        arr = [1, 3]
        state, h = move(arr, pos, state)
    elif pos==1:
        arr = [0, 2, 4]
        state, h = move(arr, pos, state)
    elif pos==2:
        arr = [1, 5]
        state, h = move(arr, pos, state)
    elif pos==3:
        arr = [0, 4, 6]
        state, h = move(arr, pos, state)
    elif pos==4:
        arr = [1, 3, 5, 7]
        state, h = move(arr, pos, state)
    elif pos==5:
        arr = [2, 4, 8]
        state, h = move(arr, pos, state)
    elif pos==6:
        arr = [3, 7]
        state, h = move(arr, pos, state)
    elif pos==7:
        arr = [4, 6, 8]
        state, h = move(arr, pos, state)
    elif pos==8:
        arr = [5, 6]
        state, h = move(arr, pos, state)
        
    print("\n------ Level "+str(Level)+" ------")
    print_in_format(state)
    print("\nHeuristic Value(Misplaced) : "+str(h))
    