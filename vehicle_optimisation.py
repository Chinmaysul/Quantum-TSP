from pulp import *
import math
items=int(input("Enter no. of items :"))
vehicles=input("Enter names of vehicles :").split()
a=len(vehicles)
cap=[]
num={}
total=0
for i in vehicles:
    x=int(input("No of {}:".format(i)))
    num[i]=x
    total+=x
for i in range(a):
    x=int(input("Capacity of {}:".format(vehicles[i])))
    cap.append(x)
rate=[]
for i in range(a):
    rate.append(int(input("Cost per round for {}:".format(vehicles[i]))))
prob=LpProblem("Vehicle_Optimisation", LpMinimize)
vars=LpVariable.dicts("No. of",[j for j in vehicles],0,cat='Integer')
# objective equation
prob+=lpSum(vars[vehicles[i]]*rate[i] for i in range(a))

# constraints
prob+=lpSum(vars[vehicles[i]]*cap[i] for i in range(a)) >= items    
for i in vehicles:
    prob+=(vars[i]) <= num[i]
ans=[]
prob.solve()
cost=0
for v in prob.variables():
    print(v,":",v.varValue)
print("Total cost=",value(prob.objective))





















