import math as m
import copy as c
def compare(puzzle,goal):
    diff=[]
    for j in range(n+1):
        rowp=0
        rowg=0
        for i in puzzle:
            try:
                if(j==0):
                    col0=i.index(j)
                    row0=rowp
                colp=i.index(j)
                break
            except:
                rowp+=1
        for i in goal:
            try:
                colg=i.index(j)
                break
            except:
                rowg+=1
        diff.append(abs(colp-colg)+abs(rowp-rowg))
    return sum(diff),row0,col0,diff
puzzle=[]
goal=[]
n=int(input("Enter n for puzzle:\t"))
w=int(m.sqrt(n+1))
h=w
num=1
print("Enter the value of bricks and 0 for blank:\n")  
for i in range(w):
    l1=[]
    for j in range(h):
        l1.append(int(input()))
    puzzle.append(l1)

for i in range(w):
    l1=[]
    for j in range(h):
        if(num==(n+1)):
           num=0
        l1.append(num)
        num+=1
    goal.append(l1)
    
treeList=[]
parentList=[{"parent":"root","puzzleN":puzzle,"after":"None"}]
oldList=[puzzle]
sequence=[puzzle]
while True:
    poppedPuzzle=sequence.pop(0)
    for d in parentList:
        if(d["puzzleN"]==poppedPuzzle):
            parentAfter=d["after"]
    result=compare(poppedPuzzle,goal)
    listOfUpdatedPuzzles=[]
    temp=poppedPuzzle[result[1]][result[2]]
    if(result[1]-1>=0 and parentAfter!="Up"):
        updatedPuzzle=c.deepcopy(poppedPuzzle)
        updatedPuzzle[result[1]][result[2]]=updatedPuzzle[result[1]-1][result[2]]
        updatedPuzzle[result[1]-1][result[2]]=temp
        if updatedPuzzle in oldList:
            pass
        else:
            parentList.append({"parent":poppedPuzzle,"puzzleN":updatedPuzzle, "after":"Down"})
            listOfUpdatedPuzzles.append(updatedPuzzle)
            oldList.append(updatedPuzzle)
    if(result[1]+1<w and parentAfter!="Down"):
        updatedPuzzle=c.deepcopy(poppedPuzzle)
        updatedPuzzle[result[1]][result[2]]=updatedPuzzle[result[1]+1][result[2]]
        updatedPuzzle[result[1]+1][result[2]]=temp
        if updatedPuzzle in oldList:
            pass
        else:
            parentList.append({"parent":poppedPuzzle,"puzzleN":updatedPuzzle, "after":"Up"})
            listOfUpdatedPuzzles.append(updatedPuzzle)
            oldList.append(updatedPuzzle)
    if(result[2]-1>=0 and parentAfter!="Left"):
        updatedPuzzle=c.deepcopy(poppedPuzzle)
        updatedPuzzle[result[1]][result[2]]=updatedPuzzle[result[1]][result[2]-1]
        updatedPuzzle[result[1]][result[2]-1]=temp
        if updatedPuzzle in oldList:
            pass
        else:
            parentList.append({"parent":poppedPuzzle,"puzzleN":updatedPuzzle, "after":"Right"})
            listOfUpdatedPuzzles.append(updatedPuzzle)
            oldList.append(updatedPuzzle)
    if(result[2]+1<w and parentAfter!="Right"):
        updatedPuzzle=c.deepcopy(poppedPuzzle)
        updatedPuzzle[result[1]][result[2]]=updatedPuzzle[result[1]][result[2]+1]
        updatedPuzzle[result[1]][result[2]+1]=temp
        if updatedPuzzle in oldList:
            pass
        else:
            parentList.append({"parent":poppedPuzzle,"puzzleN":updatedPuzzle, "after":"Left"})
            listOfUpdatedPuzzles.append(updatedPuzzle)
            oldList.append(updatedPuzzle)
            
    treeList.extend(listOfUpdatedPuzzles);
    ham=[]
    for a in treeList:
        result=compare(a,goal)
        ham.append(sum(i>0 for i in result[3]))
        index=ham.index(min(ham))
        sequence.append(treeList.pop(index))
        if(treeList==[]):
            break

    if (goal in treeList or goal in sequence):
        tree=[]
        current=goal
        while True:
            for d in parentList:
                if(d["puzzleN"]==current):
                    tree.append([d["after"],current])
                    current=d["parent"]
            if current=="root":
                for a in reversed(tree):
                    if(a[0]=="None"):
                        print "Initial Puzzle:\t",a[1],"\n" 
                    else:
                        print "After Move:\t",a[0],"\nUpdated Puzzle:\t",a[1],"\n"
                print "Total Moves:\t",len(tree)
                break
        break
    else:
            pass
