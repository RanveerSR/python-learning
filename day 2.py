age = int(input("Enter your age: "))

if age >= 18: 
    print("you are eligible to vote")
    if age <= 30:
        print("you are a youth" )
    elif age <= 50: 
        print("you are a middle aged man")
    else:
        print("you are a senior citizen")
else :
    print("you are not eligeble to vote")
    if age > 13 :
        print("you are a teenager")
    else:
        print("you are just a kid")
