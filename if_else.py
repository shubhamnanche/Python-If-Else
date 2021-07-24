n = int(input("Enter n :- "))

if (n%2 != 0) or (n%2 ==0 and 6<=n<=20):
    print("Weird 000000000")
elif (n%2 == 0 and 2<=n<=5) or (n%2 == 0 and 20<n) :
    print("Not Weird")
