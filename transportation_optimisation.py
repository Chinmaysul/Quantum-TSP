from pulp import *
source=input("Enter names of sources :").split()
dest=input("Enter names of destinations :").split()
a=len(source)
b=len(dest)
dist=[]
for i in range(a):
    temp=[]
    for j in range(b):
        x=int(input("Distance between {} and {} in kms :".format(source[i],dest[j])))
        temp.append(x)
    dist.append(temp)
supply=[]
demand=[]
for i in range(a):
    x=int(input("Supply constraint for {} :".format(source[i])))
    supply.append(x)
    
for i in range(b):
    x=int(input("Demand constraint for {} :".format(dest[i])))
    demand.append(x)

prob=LpProblem("Transportation_Optimisation", LpMinimize)
vars=LpVariable.dicts("ShippingAmount",(range(a),range(b)),0)
prob+=lpSum(vars[i][j]*dist[i][j] for i in range(a) for j in range(b))

for j in range(b):
    prob+=lpSum(vars[i][j] for i in range(a)) <= demand[j]
    
for i in range(a):
    prob+=lpSum(vars[i][j] for j in range(b)) >= supply[i]

ans=[]
prob.solve()
for v in prob.variables():
    ans.append(v.varValue)
places=[]
for i in range(a):
    for j in range(b):
        s=source[i]+" to "+dest[j]
        places.append(s)
for i in range(a*b):
    if(ans[i]>0):
        print(places[i],'=',ans[i])






















