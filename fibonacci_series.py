#Program to print fibonacci series
nterms=int(input("Enter the no. of terms to be printed:"))
#First two terms
n1,n2=0,1
count=0
if nterms<=0:
    print("Please enter a positive integer")
if nterms==1:
    print(n1)
while count<nterms:
    print(n1)
    nth=n1+n2
    #new values
    n1=n2
    n2=nth
    count+=1