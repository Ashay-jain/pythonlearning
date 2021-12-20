n=int(input("enter any no."))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("the no. is a prime no.",n)
        break