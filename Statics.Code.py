##A beam AB is subjected to several vertical forces as shown.\
##Write a computer program that can be used to determine the magnitude of the resultant of the forces and the distance x C to point C,
##the point where the line of action of the resultant intersects AB.
print("**Mohammad Amin Labbaf/Student ID=99154761/Major=Aerospace engineering**")
print("**Please pay attention to the direction of the force, (upward is positive direction)**")
count=int(input('Enter the count of the forces= '))

##Make lists for the entered forces and distances
ls_forces=[]
ls_distance=[]

for i in range(1,count+1):
    x=float(input("Please enter the force= "))
    ls_forces.append(x)
    y=float(input("Please enter the distance from the origin to the entered force= "))
    ls_distance.append(y)
    
##Make lists for Moment
ls_moment=[]

##By utlizing the loop we determine the moment=d*F
for i in range(0,count):
    M=(ls_forces[i]*ls_distance[i])
    ls_moment.append(M)
    
Sum_F=sum(ls_forces)
Sum_MOMENT=sum(ls_moment)
Answer=Sum_MOMENT/Sum_F

print(f"The resultant of the forces and the distance xC ={Answer}")
